#!/usr/bin/env bash
# get_gemma_q4km.sh — Bash downloader for gemma-3-1b-it-q4_k_m.gguf
# Examples:
#   HF_TOKEN=hf_xxx ./get_gemma_q4km.sh
#   HF_TOKEN=hf_xxx ./get_gemma_q4km.sh -d ./gguf --verify
#   HF_TOKEN=hf_xxx ./get_gemma_q4km.sh --mirror https://huggingface.co/someone/repo/resolve/main
#   ./get_gemma_q4km.sh --public --sha256 8270790f3ab6...   # verify with a known hash

set -euo pipefail

# ---------------- Defaults ----------------
DEST_DIR="${DEST_DIR:-models}"
# Try both common filenames (some repos use uppercase underscores)
CANDIDATE_FILES=(
  "gemma-3-1b-it-q4_k_m.gguf"
  "gemma-3-1b-it-Q4_K_M.gguf"
)
MIRRORS=(
  "https://huggingface.co/unsloth/gemma-3-1b-it-GGUF/resolve/main"
  "https://huggingface.co/bartowski/google_gemma-3-1b-it-GGUF/resolve/main"
  "https://huggingface.co/lmstudio-community/gemma-3-1b-it-GGUF/resolve/main"
  "https://huggingface.co/DravenBlack/gemma-3-1b-it-Q4_K_M-GGUF/resolve/main"
  "https://huggingface.co/mradermacher/gemma-3-1b-it-GGUF/resolve/main"
)
RETRIES="${RETRIES:-5}"
QUIET=false
FORCE=false
VERIFY=false
PUBLIC=false
EXPECTED_SHA=""

# --------------- Helpers ------------------
log() { [[ "$QUIET" == true ]] || printf '%s\n' "$*"; }
err() { printf '%s\n' "$*" >&2; }
have() { command -v "$1" >/dev/null 2>&1; }

sha256_of() {
  if have sha256sum; then sha256sum "$1" | awk '{print $1}'
  elif have shasum; then shasum -a 256 "$1" | awk '{print $1}'
  else
    err "❌ No sha256sum/shasum available."; return 1
  fi
}

fetch_sidecar_sha() {
  # Try ${file}.sha256 next to the file URL
  local base="$1" file="$2" token="${3:-}" tmp
  tmp="$(mktemp -t gemma.sha.XXXXXX)"
  if have curl; then
    local curl_args=(-fsSL)
    [[ -n "$token" ]] && curl_args+=(-H "Authorization: Bearer ${token}")
    if curl "${curl_args[@]}" "${base%/}/${file}.sha256" -o "$tmp"; then
      grep -Eo '[A-Fa-f0-9]{64}' "$tmp" | head -n1
      rm -f "$tmp"; return 0
    fi
  elif have wget; then
    local wget_args=(-q)
    [[ -n "$token" ]] && wget_args+=(--header="Authorization: Bearer ${token}")
    if wget "${wget_args[@]}" -O "$tmp" "${base%/}/${file}.sha256"; then
      grep -Eo '[A-Fa-f0-9]{64}' "$tmp" | head -n1
      rm -f "$tmp"; return 0
    fi
  fi
  rm -f "$tmp" 2>/dev/null || true
  return 1
}

download_with_resume() {
  local url="$1" dest="$2" token="${3:-}"
  local tmp="${dest}.part"

  if have curl; then
    local curl_args=(-fL --retry "$RETRIES" --retry-delay 2 --retry-all-errors -C - -o "$tmp")
    [[ -n "$token" ]] && curl_args+=(-H "Authorization: Bearer ${token}")
    curl "${curl_args[@]}" "$url"
  elif have wget; then
    local wget_args=(-c --tries="$RETRIES" -O "$tmp")
    [[ -n "$token" ]] && wget_args+=(--header="Authorization: Bearer ${token}")
    wget "${wget_args[@]}" "$url"
  else
    err "❌ Neither curl nor wget is installed."
    return 2
  fi
  mv -f "$tmp" "$dest"
}

verify_sha() {
  local file="$1" expect="$2"
  local actual; actual="$(sha256_of "$file")" || return 1
  # bash lowercase
  if [[ "${actual,,}" != "${expect,,}" ]]; then
    err "❌ SHA256 mismatch for $(basename "$file")"
    err "   expected: $expect"
    err "   actual  : $actual"
    return 2
  fi
  log "✅ SHA256 verified: $file"
}

usage() {
  cat <<'USAGE'
Usage: get_gemma_q4km.sh [options]
Options:
  -d, --dest DIR          Destination directory (default: models)
  -m, --mirror URL        Add an extra mirror (can repeat)
  -t, --token TOKEN       Hugging Face token (default: $HF_TOKEN)
      --public            Allow downloads without a token
  -f, --force             Re-download even if file exists
  -q, --quiet             Less logging
  -v, --verify            Verify SHA256 (tries sidecar *.sha256)
      --sha256 HEX        Provide expected SHA256 explicitly
  -h, --help              Show help
USAGE
}

# --------------- Parse args ---------------
HF_TOKEN="${HF_TOKEN:-}"
declare -a extra_mirrors=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    -d|--dest) DEST_DIR="$2"; shift 2 ;;
    -m|--mirror) extra_mirrors+=("$2"); shift 2 ;;
    -t|--token) HF_TOKEN="$2"; shift 2 ;;
    --public) PUBLIC=true; shift ;;
    -f|--force) FORCE=true; shift ;;
    -q|--quiet) QUIET=true; shift ;;
    -v|--verify) VERIFY=true; shift ;;
    --sha256) EXPECTED_SHA="$2"; VERIFY=true; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    --) shift; break ;;
    *) err "Unknown option: $1"; usage; exit 2 ;;
  esac
done

if [[ ${#extra_mirrors[@]} -gt 0 ]]; then
  MIRRORS+=("${extra_mirrors[@]}")
fi

# Token requirement unless --public
if [[ "$PUBLIC" == false && -z "${HF_TOKEN}" ]]; then
  err "Error: HF_TOKEN is not set. Export HF_TOKEN or pass --token, or use --public to skip."
  exit 1
fi

mkdir -p -- "$DEST_DIR"
log "📁 Destination: $DEST_DIR"
log "🌐 Mirrors:"; for m in "${MIRRORS[@]}"; do log "   - $m"; done
[[ "$VERIFY" == true ]] && log "🔒 Verification enabled."

ok=false
target=""

for fname in "${CANDIDATE_FILES[@]}"; do
  for base in "${MIRRORS[@]}"; do
    url="${base%/}/${fname}"
    target="${DEST_DIR%/}/${fname}"

    if [[ -f "$target" && "$FORCE" == false ]]; then
      log "✅ Exists: $target (use --force to re-download)"
      if [[ "$VERIFY" == true ]]; then
        exp="$EXPECTED_SHA"
        if [[ -z "$exp" ]]; then
          exp="$(fetch_sidecar_sha "$base" "$fname" "$HF_TOKEN" || true)"
        fi
        if [[ -n "$exp" ]]; then
          if ! verify_sha "$target" "$exp"; then
            err "Existing file failed verification."
            exit 2
          fi
        fi
      fi
      ok=true; break
    fi

    log "⬇️  Downloading: $url"
    if download_with_resume "$url" "$target" "${HF_TOKEN:-}"; then
      log "✅ Saved: $target"
      if [[ "$VERIFY" == true ]]; then
        exp="$EXPECTED_SHA"
        if [[ -z "$exp" ]]; then
          exp="$(fetch_sidecar_sha "$base" "$fname" "$HF_TOKEN" || true)"
        fi
        if [[ -n "$exp" ]]; then
          if ! verify_sha "$target" "$exp"; then
            mv -f "$target" "${target}.bad.$(date +%s)"
            continue
          fi
        else
          log "ℹ️  No sidecar SHA found; skipped verification."
        fi
      fi
      ok=true; break
    else
      err "❌ Failed from this mirror; trying next…"
      [[ -f "$target.part" ]] && rm -f "$target.part"
    fi
  done
  [[ "$ok" == true ]] && break
done

if [[ "$ok" != true ]]; then
  err "💥 All attempts failed for candidates: ${CANDIDATE_FILES[*]}"
  exit 1
fi

log "🎉 Done."

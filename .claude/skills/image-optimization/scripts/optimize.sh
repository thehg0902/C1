#!/usr/bin/env bash
# Usage: optimize.sh <input> [max-width]
# Requires cwebp (images) / ffmpeg (video). Prints commands it runs + sizes.
set -e
IN="$1"; W="${2:-1440}"
[ -f "$IN" ] || { echo "no such file: $IN" >&2; exit 1; }
BASE="${IN%.*}"; EXT="${IN##*.}"
case "$EXT" in
  jpg|jpeg|png)
    command -v cwebp >/dev/null || { echo "cwebp missing - run locally: cwebp -q 80 -resize $W 0 '$IN' -o '${BASE}.webp'"; exit 2; }
    cwebp -q 80 -resize "$W" 0 "$IN" -o "${BASE}.webp"
    ls -l "$IN" "${BASE}.webp" ;;
  mp4|mov|webm)
    command -v ffmpeg >/dev/null || { echo "ffmpeg missing - run locally: ffmpeg -i '$IN' -an -c:v libx264 -crf 24 -movflags +faststart -vf scale=-2:1080 '${BASE}-web.mp4'"; exit 2; }
    ffmpeg -y -i "$IN" -an -c:v libx264 -crf 24 -movflags +faststart -vf "scale=-2:1080" "${BASE}-web.mp4"
    ffmpeg -y -sseof -0.1 -i "${BASE}-web.mp4" -frames:v 1 "${BASE}-poster.png"
    command -v cwebp >/dev/null && cwebp -q 80 "${BASE}-poster.png" -o "${BASE}-poster.webp" && rm "${BASE}-poster.png"
    ls -l "$IN" "${BASE}-web.mp4" ;;
  *) echo "unsupported: $EXT" >&2; exit 1 ;;
esac

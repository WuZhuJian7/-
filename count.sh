#!/bin/bash
cd "$(dirname "$0")/content" || exit 1
for f in "$@"; do
  c=$(grep -v '^#' "$f" | grep -v '完）——' | tr -d '[:space:]' | wc -m)
  flag=""
  if [ "$c" -lt 1500 ] || [ "$c" -gt 3000 ]; then flag="  <== 超范围"; fi
  echo "$f : $c$flag"
done

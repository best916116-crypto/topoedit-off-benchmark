#!/usr/bin/env bash
set -euo pipefail

cd "/home/pjj/workspace/topoedit-off-benchmark_public_release"

git init
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/best916116-crypto/topoedit-off-benchmark.git

git add .
git commit -m "Prepare TopoEdit-Off benchmark public release package v0.67E" || true
git push -u origin main

git tag -a v0.67E -m "TopoEdit-Off benchmark public release package v0.67E"
git push origin v0.67E

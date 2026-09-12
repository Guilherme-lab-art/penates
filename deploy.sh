#!/bin/bash
# Pénates → URL ao vivo na Vercel.
# Uso:  VERCEL_TOKEN=seu_token_aqui ./deploy.sh
set -e
cd "$(dirname "$0")"
[ -z "$VERCEL_TOKEN" ] && { echo "✗ export VERCEL_TOKEN=... antes (me peça no chat que eu publico)"; exit 1; }
mkdir -p dist && cp index.html dist/
npx --yes vercel deploy dist --prod --confirm --token "$VERCEL_TOKEN"

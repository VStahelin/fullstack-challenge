#!/bin/bash
set -e

if [ -n "$1" ]; then
    exec "$@"
fi

npm rebuild esbuild

npm run dev

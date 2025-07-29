#!/bin/bash

# runner.sh - Utility script
#
# Usage:
#   ./runner.sh [extract|test|submit|help]
#
# Options:
#   extract   Extract libc and build binary
#   test      Build and run the challenge locally
#   submit    Submit the payload to the remote
#   help      Show this help message

set -e

show_help() {
    grep '^#' "$0" | cut -c 4-
}

extract() {
    echo "[+] Extracting libc and building binary..."
    id=$(docker create ubuntu:22.04@sha256:3c61d3759c2639d4b836d32a2d3c83fa0214e36f195a3421018dbaaf79cbe37f)
    docker cp "$id":/lib/x86_64-linux-gnu/libc.so.6 ./libc.so.6
    docker rm -v "$id"
    
    docker build . -t test
    docker run --privileged test kctf_drop_privs python3 -c 'from common import build, run; from base64 import b64encode; print(b64encode(build()).decode())' | base64 -d > runtime
    chmod +x runtime
    echo "[+] Extracted to ."
}

test_run() {
    echo "[+] Building and running the challenge locally..."
    docker build . -t test
    docker run --privileged test kctf_drop_privs python3 -c 'from common import build, run; run(build())'
}

submit() {
    echo "$(cat src/payload/src/payload.rs | base64 -w 0)" | nc chal.wwctf.com 7004
}

case "$1" in
    extract)
        extract
        ;;
    test)
        test_run
        ;;
    submit)
        submit
        ;;
    help|--help|-h|"")
        show_help
        ;;
    *)
        echo "Unknown option: $1" >&2
        show_help
        exit 1
        ;;
esac
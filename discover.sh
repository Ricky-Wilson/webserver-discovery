#!/bin/bash

nmap \
    --host-timeout 10s \
    --max-retries 0 \
    –min-parallelism 100 \
    -T5 \
    -Pn \
    -n \
    -iR "$1" \
    -p80 \
    -oG tmp.txt \
    --open \
    tmp.txt > /dev/null
    awk '/Host/ {print $2}' tmp.txt
    rm tmp.txt

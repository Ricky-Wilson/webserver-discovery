#!/bin/bash

nhosts=$1

nmap \
--host-timeout 10s \
--max-retries 0 \
–min-parallelism 100 \
-T5 \
-Pn \
-n \
-iR $1 \
-p80 \
-oG tmp.txt \
--open \
tmp.txt > /dev/null

cat tmp.txt | grep 'Host' | awk '{print $2}'
rm tmp.txt
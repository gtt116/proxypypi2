#!/bin/bash

MIRROR_DIR=/home/data/mirrors/
INDEX_URL=http://pypi.douban.com/simple

proxypypi2  -P proxypypi2.pid -l proxypypi2.log -o proxypypi2.console \
    -d $MIRROR_DIR \
    -i $INDEX_URL\
    -p 8081 $1

#!/usr/bin/env bash

docker run -t -i -p 8089:8089 -v $PWD:/root/loader mooxe/python

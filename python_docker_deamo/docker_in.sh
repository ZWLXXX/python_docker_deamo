#!/usr/bin/env bash

docker run -t -i -p 8089:8089 --privileged=true -v $PWD:/root/loader mooxe/python

#!/bin/bash

tar xvf netperf-2.7.0.tar.gz

cd netperf-netperf-2.7.0

./configure --build=arm-linux

make 

make install



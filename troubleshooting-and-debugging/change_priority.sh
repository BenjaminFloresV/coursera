#!/bin/bash

for pid in $(pidof ffmepg); do renice 19 $pid; done

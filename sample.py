#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

# 192.168.99.100'
host = '172.17.0.1'
args = ['ping', '-c 3', host]

try:
#  res1 = subprocess.check_call(args)
  res = subprocess.check_output(args)
except:
  res = "Error. (" + host + ")"

#print res1
print res

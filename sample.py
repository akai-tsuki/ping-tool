#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

args = ['ping', '-c 3', '192.168.99.100']

try:
  res1 = subprocess.check_call(args)
  res2 = subprocess.check_output(args)
except:
  print "Error."

print res1
print res2

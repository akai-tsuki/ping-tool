#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

# host = '172.17.0.1'
hosts = ['172.17.0.1', '172.17.0.2', '192.168.99.100']

for host in hosts:
  args = ['ping', '-c 3', host]

  try:
  #  res = subprocess.check_call(args)
    res = subprocess.check_output(args)
  except:
    res = "Error. (" + host + ")"
  
  print res

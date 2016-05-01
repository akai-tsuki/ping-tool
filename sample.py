#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging
import logging.config

import argparse

parser = argparse.ArgumentParser(description='This is tool sample.')
parser.add_argument('-t', '--tool', type=str, help='tool name')
args = parser.parse_args()

logging.config.fileConfig("./conf/logging.conf")
logger = logging.getLogger("pingApp")

hosts = ['172.17.0.1', '172.17.0.2', '192.168.99.100']

for host in hosts:
  args = ['ping', '-c 1', host]

  try:
  #  res = subprocess.check_call(args)
    res = subprocess.check_output(args)
  except:
    res = "Error. (" + host + ")"
  
  logger.debug('test ------- mesage')
  
  for line in res.splitlines():
    logger.info(line)


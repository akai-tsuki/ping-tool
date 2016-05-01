#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging
import logging.config
import datetime
import argparse


today = datetime.datetime.today()

parser = argparse.ArgumentParser(description='This is tool sample.')
parser.add_argument('-t', '--tool', type=str, help='tool name')
args = parser.parse_args()


logging.config.fileConfig("./conf/logging.conf")
logger = logging.getLogger("pingApp")
console_out = logging.getLogger("console")

start_time = today.strftime("%Y/%m/%d %H:%M:%S")
console_out.info("start : " + start_time)


if args.tool is not None:
  console_out.info("tool : " + args.tool)

logger.debug('ping check : start')

hosts = ['172.17.0.1', '172.17.0.2', '192.168.99.100']

for host in hosts:
  args = ['ping', '-c 1', host]

  try:
  #  res = subprocess.check_call(args)
    res = subprocess.check_output(args)
  except:
    res = "Error. (" + host + ")"
  
  for line in res.splitlines():
    logger.info(line)


console_out.info("end")

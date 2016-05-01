#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging
import logging.config
import datetime
import argparse

# logger
logging.config.fileConfig("./conf/logging.conf")
logger = logging.getLogger("pingApp")
console_out = logging.getLogger("console")

def test():
  print "call test"

def doPing(hosts):
  logger.debug('ping check : start')
  
  for host in hosts:
    args = ['ping', '-c 1', host]
  
    try:
    #  res = subprocess.check_call(args)
      res = subprocess.check_output(args)
    except:
      res = "Error. (" + host + ")"
    
    for line in res.splitlines():
      logger.info(line)



if __name__ == "__main__":
  hosts = ['172.17.0.1', '172.17.0.2', '192.168.99.100']
  
  today = datetime.datetime.today()
  
  parser = argparse.ArgumentParser(description='This is tool sample.')
  parser.add_argument('-t', '--tool', type=str, help='tool name')
  args = parser.parse_args()
  
  start_time = today.strftime("%Y/%m/%d %H:%M:%S")
  console_out.info("start : " + start_time)
  
  if args.tool is not None:
    console_out.info("tool : " + args.tool)
    
    if args.tool == 'ping':
      doPing(hosts)
  
  
  console_out.info("end")

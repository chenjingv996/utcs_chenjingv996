#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math
import os
from logzero import logger,logfile

print(f"{time.ctime()}\n")
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

print(os.system("pwd\n"))
print(os.system("chenjingv\n"))


logger.debug("hello111")

logger.info("info222")

logger.warning("warning333")

logger.error("error444")

logfile('./test_logger.log',maxBytes=1e6,backupCount=5)

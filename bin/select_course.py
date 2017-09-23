#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author = "susu"
import os
import sys
from core.mains import *
from core.models import *
from core.teacher import *
from core.student import *
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )# 取目录路径
sys.path.append(BASE_DIR)
if __name__ == '__main__':
    run()


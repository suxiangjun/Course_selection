#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author = "susu"
import pickle,sys
from core.teacher import *
from core.student import *
from core.admin import *
import os
import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )# 取目录路径
sys.path.append(BASE_DIR)

def run():
    for i in range(3):
        choice = input("请选择身份\n1、我是学生\n2、我是教师\n3、我是管理员\n>>")
        if choice=="1":
            main_student()
            continue
        elif choice=="2":
            main_teacher()
            continue
        elif choice=="3":
            main_admin()
            continue
        elif choice=="q":
            break
        else:
            print("输入有误，请重新输入！")
    else:
        print("输入次数超过3次，再见！")
        sys.exit()



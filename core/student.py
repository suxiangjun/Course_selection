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
#注册学员
def create_student():
    name=input("姓名：")
    age=input("年龄：")
    sex=input("性别：")
    for i in range(3):
        password1=input("密码：")
        password2=input("请再输入密码：")
        if password1 != password2:
            print("密码输入错误，请重新输入。")
            continue
        else:
            g=view_obj(Grade)
            choice = input("请选择班级:")
            if choice in g:
                g=Student(name,age,sex,password1,g[choice])
                print("恭喜\033[1;31m%s\033[0m，注册成功！"% name)
                print("请记住你的学号\033[1;31m%s\033[0m"%g.account)
                break
    else:
        print("输入次数超过3次.")

#登陆装饰器
def auth(fun):
    def deco():#装饰函数
        print("\033[1;32m#####欢迎登陆学生选课系统#####\033[0m")
        username=input("学号：")
        s=dict_student()
        if username in s:
            for i in range(3):
                Password=input("密码：")
                if s[username].password==Password:
                    fun(s[username])
                    break
            else:
                print("密码输入3次，再见！")
                sys.exit()

        else:
            print("账号不存在，请注册。")
            create_student()
    return deco#返回装饰函数的内存地址

#交学费
@auth
def main_student(s):
    while True:
        choice = input("1、我的资料\n2、交学费\n3、选择班级\n>>")
        if choice=="1":
            d = s.__dict__
            for key in d:
                print("\033[1;31m%s\033[0m: %s" % (key, d[key]))
        elif choice=="2":
            s.pay_tuition()
        elif choice=="3":
            c=s.choice_grade()
            dict_class()[c].add_student(s)
        elif choice=="b":
            sys.exit()
        else:
            break










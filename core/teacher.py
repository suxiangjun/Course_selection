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
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )# 取目录路径
sys.path.append(BASE_DIR)
#登陆验证
def auth(fun):
    def deco():#装饰函数
        print("\033[1;32m#####欢迎登陆教师管理系统#####\033[0m")
        username=input("账号：")
        t=dict_teacher()
        if username in t:
            if t[username].password=="123":
                print("默认密码为：\033[1;31m%s\033[0m\n请修改密码。"%"123")
                for i in range(3):
                    password1 = input("新密码：")
                    password2 = input("请再输入密码：")
                    if password1 != password2:
                        print("密码输入错误，请重新输入。")
                        continue
                    t[username].change_password(password1)
                    fun(t[username])
                else:
                    print("输入次数超过3次.")
                    sys.exit()
            else:
                for i in range(3):
                    password=input("密码：")
                    if t[username].password ==password:
                        fun(t[username])
                        sys.exit()
                    else:
                        print("密码错误，请重新输入。")
                else:
                    print("输入次数超过3次.")
                    sys.exit()
        else:
            print("账号不存在，请找管理员获取。")
    return deco#返回装饰函数的内存地址

#老师教的班级
def teacher_ID_grade_studens(t):
    c=[]
    for i in Grade.get_obj():
        if i.teacher.account==t.account:
            c.append(i)
    return c
@auth
def main_teacher(t):
    while True:
        choice = input("1、我的资料\n2、我的班级\n3、我的学生\n>>")
        if choice=="1":
            d = t.__dict__
            for key in d:
                print("\033[1;31m%s\033[0m: %s" % (key, d[key]))
        elif choice=="2":
            for i in teacher_ID_grade_studens(t):
                print("\033[1;31m%s\033[0m"% i)
        elif choice=="3":
            if  teacher_ID_grade_studens(t):
                for j in teacher_ID_grade_studens(t):
                    b=" ".join(list(j.student.keys()))
                    print('''========%s========
\033[1;31m%s\033[0m'''%(j,b))
            else:
                print("抱歉，暂时没有选课的学生")
        elif choice=="b":
            sys.exit()
        else:
            break



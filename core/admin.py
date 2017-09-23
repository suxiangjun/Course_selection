#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author = "susu"
import os
import pickle
import uuid
import time
import re
import sys
from core.mains import *
from core.models import *
from core.teacher import *
from core.student import *
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )# 取目录路径
sys.path.append(BASE_DIR)
#创建学校
def create_school():
    while True:
        choice1=input("1、查看学校\n2、新建学校\n3、删除学校\n>>")
        if choice1=="1":
            view_obj(School)
        elif choice1=="2":
            name=input("学校名字：")
            if name=="q":
                break
            city=input("分校城市：")
            if city=="q":
                break
            s=School(name,city)
            print("已成功创建:\033[1;31m%s%s分校\033[0m"%(name,city))
        elif choice1=="3":
            try:
                del_school=input("请输入需要删除的学校名字：")
                os.remove(basedir + "school/"+del_school)
            except FileNotFoundError as e:
                print("学校不存在，请重新输入。")
        else:
            break

# 创建课程
def create_course():
    while True:
        choice1 = input("1、查看课程\n2、新建课程\n3、删除课程\n>>")
        if choice1 == "1":
            view_obj(Course)
        elif choice1 == "2":
            d = view_obj(School)
            choice2 = input("学校名字：")
            if choice2 in d:
                c = Course(d[choice2])
                print("课程创建成功")
            else:
                print("课程创建失败")
        elif choice1 == "3":
            try:
                del_course = input("请输入需要删除的课程名字：")
                os.remove(basedir + "course/" + del_course)
            except FileNotFoundError as e:
                print("课程不存在，请重新输入。")
        else:
            break

#创建讲师
def create_teacher():
    while True:
        choice1 = input("1、查看讲师\n2、新建讲师\n3、删除讲师\n>>")
        if choice1 == "1":
            view_obj_teacher(Teacher)
        elif choice1 == "2":
            name=input("姓名：")
            if name=="q" or name==0:
                break
            age=input("年龄：")
            if age=="q" or name==0:
                break
            sex=input("性别：")
            if sex=="q" or name==0:
                break
            d = view_obj(Course)
            choice2 = input("讲师教授的课程：")
            if choice2=="q" or choice2==0:
                break
            if choice2 in d:
                s = Teacher(name,age,sex,d[choice2])
                print("讲师创建成功")
            else:
                print("讲师创建失败")
        elif choice1 == "3":
            try:
                del_teacher = input("请输入需要删除的讲师名字：")
                os.remove(basedir + "course/" + del_teacher)
            except FileNotFoundError as e:
                print("讲师不存在，请重新输入。")
        else:
            break

#创建班级
def create_class():
    while True:
        choice1 = input("1、查看班级\n2、新建班级\n3、删除班级\n>>")
        if choice1 == "1":
            view_obj(Grade)
        elif choice1 == "2":
            c = view_obj(Course)
            choice2 = input("课程名字：")
            if choice2=="q" or choice2==0:
                break
            t= course_teacher(choice2)
            choice3=input("请从上面选择一位授课讲师：")
            if choice3=="q" or choice2==0:
                break
            if choice2 in c and choice3 in t:
                g = Grade(c[choice2],t[choice3])
                print("班级创建成功")
            else:
                print("班级创建失败")
        elif choice1 == "3":
            try:
                del_class = input("请输入需要删除的班级名字：")
                os.remove(basedir + "class/" + del_class)
            except FileNotFoundError as e:
                print("班级不存在，请重新输入。")
        else:
            break

#初始化
def clear_all():
    for i in os.listdir(basedir):
        for j in os.listdir(basedir + i):
            os.remove(basedir + i + "/" + j)
    pickle.dump(2018100, open(dir_student_account, "wb"))
    pickle.dump(101, open(dir_student_account, "wb"))

def main_admin():
    while True:
        choice = input("请选择想要操作的对象\n1、学校\n2、课程\n3、讲师\n4、班级\n5、初始化数据\n>>")
        if choice == "1":
            create_school()
        elif choice == "2":
            create_course()
        elif choice == "3":
            create_teacher()
        elif choice == "4":
            create_class()
        elif choice == "5":
            clear_all()
        elif choice=="b":
            sys.exit()
        else:
            break


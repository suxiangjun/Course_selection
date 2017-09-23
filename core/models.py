#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author = "susu"
import pickle
import os
import sys
import uuid
import re
import os
import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
from core.mains import *
from core.teacher import *
from  core.models import *
basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/db/"
dir_student_account = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
           + "/conf/student_account.conf"
dir_teacher_account=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
           + "/conf/teacher_account.conf"

#字典的形式返回对象
def view_obj(a):
    try:
        d={}
        for i in a.get_obj():
            print('\033[1;31m%s\033[0m' % i)
            d[i.name]=i
        return d
    except AttributeError as e:
        print("无记录。")

def view_obj_teacher(a):
    try:
        d = {}
        for i in a.get_obj():
            print('ID:%s    姓名：\033[1;31m%s\033[0m' % (i.account, i.name))
            d[i.name] = i
        return d
    except AttributeError as e:
        print("无记录。")
#字典返回{班级：班级对象}
def dict_class():
    g = {}
    for i in Grade.get_obj():
        g[i.name]=i
    return g
#字典返回{学号：学生对象}
def dict_student():
    s = {}
    for i in Student.get_obj():
        s[i.account]=i
    return s
#字典返回{讲师账号：讲师对象}
def dict_teacher():
    t= {}
    for i in Teacher.get_obj():
        t[i.account]=i
    return t

# 字典返回{讲师姓名：讲师对象}
def course_teacher(class_name):
    t1 = {}
    t2={}
    d={}
    #{讲师姓名：讲师对象}
    for i in Teacher.get_obj():
        t1[i.name] = i
    #{讲师id：讲师对象}
    for j in Teacher.get_obj():
        t2[j.account] = j
    for h in os.listdir(basedir + "/teacher"):
        if class_name in t2[h].course:
            d[t2[h].name]=t2[h]
            print(t2[h].name)
    return d

#创建ID号
def create_id():
    return str(uuid.uuid1())
#学校
class School(object):
    """学校类"""
    def __init__(self,name,city):
        self.city = city
        self.name=name+city+"分校"
        self.id=create_id()
        self.create_school()
    def create_school(self):
        pickle.dump(self,open(basedir+"school/"+self.name,"wb"))
    def only_course(self):
        if  self.city=="北京":
            tag=True
            while tag:
                choice=input("你选择\n1.Linux课程\n2.Python课程\n>>")
                if choice.isdigit():
                    if choice=="1" or choice=="Linux课程":
                        return {"name":"北京Linux课程","price":11000,"cycle":"3months","addr":"北京"}
                        tag=False
                    elif choice=="2" or choice=="Python课程":
                        return {"name":"北京Python课程","price":13000,"cycle":"4months","addr":"北京"}
                        tag = False
                elif choice == "q":
                    break
                else:
                    print("输入错误，请重新输入")

        elif self.city=="上海":
            return {"name":"上海Go语言课程","price":12000,"cycle":"4months","addr":"上海"}
    @staticmethod
    def get_obj():
        ret = []
        for i in os.listdir(basedir+"school"):
            ret.append(pickle.load(open(basedir+"school/"+i, "rb")))
        return ret
    def __str__(self):
        return self.name

#课程--关联学校
class Course(object):
    '''课程'''
    def __init__(self,school_obj):
        cource_dict=school_obj.only_course()
        self.school=school_obj.name
        self.name=cource_dict["name"]
        self.price=cource_dict["price"]
        self.cycle=cource_dict["cycle"]
        self.addr=cource_dict["addr"]
        self.create_course()
    def create_course(self):
        pickle.dump(self,open(basedir+"course/" + self.name,"wb"))

    @staticmethod
    def get_obj():
        ret = []
        for i in os.listdir(basedir+"course"):
            ret.append(pickle.load(open(basedir+"course/"+i, "rb")))
        return ret
    def __str__(self):
        return self.name

#班级--关联课程 讲师
class Grade(object):
    '''班级'''
    def __init__(self,course_obj,teacher_obj):
        self.course=course_obj.name
        self.name=course_obj.name+self.grade_name()
        self.teacher=teacher_obj
        self.uid=create_id()
        self.student={}
        self.create_grade()
        self.school=course_obj.school
    def create_grade(self):
        pickle.dump(self, open(basedir + "class/"+self.name, "wb"))
        print("ok")
    def add_student(self,student_obj):
        self.student[student_obj.name]=student_obj
        pickle.dump(self, open(basedir + "class/" + self.name, "wb"))
        print("选课成功！")
    def grade_name(self):
        if not os.listdir(basedir+"class"):
            return "1班"
        else:
            ret=[]
            for i in os.listdir(basedir+"class"):
                a=re.search("{}".format(self.course),i.strip())
                ret.append(a)
            return str(len(ret)+1)+"班"

 # 成员基类
    @staticmethod
    def get_obj():
        ret = []
        for i in os.listdir(basedir + "class"):
            ret.append(pickle.load(open(basedir + "class/" + i, "rb")))
        return ret
    def __str__(self):
        return self.name

#学校成员基类
class SchoolMember(object):
    '''学校成员基类'''
    def __init__(self,name,age,sex):
        self.name=name
        self.sex=sex
        self.age=age
        self.id=create_id()

#讲师--关联学校
class Teacher(SchoolMember):
    "讲师类"
    def __init__(self,name,age,sex,course_obj):
        super(Teacher,self).__init__(name,age,sex)
        self.school=course_obj.school
        self.course=[course_obj.name]
        self.password="123"
        self.create_account()
        self.create_teacher()
    def create_teacher(self):
        pickle.dump(self, open(basedir + "teacher/" + self.account, "wb"))
    def teaching_info(self):
        "讲师介绍"
        print("{}老师在{}授{}课".format(self.name,self.school,self.course))
    def create_account(self):
        a=pickle.load(open(dir_teacher_account, "rb"))
        pickle.dump(a+1, open(dir_teacher_account, "wb"))
        self.account=str(a+1)
    def change_password(self,Password):
        self.password=Password
        pickle.dump(self, open(basedir + "teacher/" + self.account, "wb"))
        print("密码修改成功")
    @staticmethod
    def get_obj():
        ret = []
        for i in os.listdir(basedir + "teacher"):
            ret.append(pickle.load(open(basedir + "teacher/" + i, "rb")))
        return ret
    def __str__(self):
        return self.name

#学生--关联班级
class Student(SchoolMember):
    def __init__(self,name,age,sex,password,grade_obj):
        super(Student, self).__init__(name,age,sex)
        self.grade=[grade_obj.name]
        self.password=password
        self.tuition = "未交学费"
        self.create_account()
        self.create_student()

    def create_student(self):
        pickle.dump(self, open(basedir + "student/" + self.account, "wb"))
    def pay_tuition(self):
        print("恭喜你，已缴清学费。")
        self.tuition="交清学费"
        pickle.dump(self, open(basedir + "student/" + self.account, "wb"))
    def choice_grade(self):
        g = view_obj(Grade)
        choice = input("请选择上课的班级:")
        if choice in g:
            self.grade.append(choice)
            pickle.dump(self, open(basedir + "student/" + self.account, "wb"))
        return choice
    def create_account(self):
        a=pickle.load(open(dir_student_account, "rb"))
        pickle.dump(a+1, open(dir_student_account, "wb"))
        self.account=str(a+1)
    @staticmethod
    def get_obj():
        ret = []
        for i in os.listdir(basedir + "student"):
            ret.append(pickle.load(open(basedir + "student/" + i, "rb")))
        return ret
    def __str__(self):
        return self.name


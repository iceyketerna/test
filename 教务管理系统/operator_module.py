import sys
from operator_module import *
import datetime
import logging

current_datetime = datetime.datetime.now

class Student:
    """
    @param
        创建学生类
    """
    def __init__(self, ID, name, age):
        self.ID = ID
        self.name = name
        self.age = age

    def __str__(self):
        return f"学生 ID:{self.ID}, 姓名:{self.name},年龄{self.age}"
class StudentManagementSystem:
    """
    @param
        创建学生管理系统类
    """
    def __init__(self):
        self.students = []

    def add_student(self, student):
        """
        @param
            增加学生信息
        """
        self.students.append(student)

    def remove_student(self,ID):
        """
        @param
            移除学生信息
        """
        for student in self.students:
            if (student.ID == ID):
                self.students.remove(student)
                return True
        return False

    def list_student(self):
        """
        @param
            列出所有学生信息
        """
        return self.students
    
    def sercher_student(self,ID):
        """
        @param
            查找指定学生信息
        """
        for student in self.students:
            if (student.ID == ID):
                print(student)
                return True
        return False


sms = StudentManagementSystem()


def operate(choice):
    """
        @param
            程序主函数
        """
    n = 0
    students = sms.list_student()
    try:
        if choice == "1":
            n = 1
            print("请输入要添加的学生的信息：")
            ID = int(input("ID:"))
            name = str(input("姓名:"))
            age = int(input("年龄："))
            if len(sms.list_student()) != 0:
                for student in students:
                    if student.ID == ID:
                        print("当前ID已存在\n")
                        return  True
            student = Student(ID,name,age)
            sms.add_student(student)
            print("学生已添加")
            print("\n")
    except:
        error_msg = f"[ERROR] [{current_datetime}]: ValueError msg in line {sys.exc_info()[2].tb_lineno},"
        logging.error(error_msg)
        print("请输入正确的ID/姓名/年龄")
        print("\n")
    try:
        if choice == "2":
            n = 1
            ID = int(input("请输入要删除的学生信息的ID："))
            if sms.remove_student(ID):
                print("学生已删除")
            else:
                print("未找到该学生")
            print("\n")
    except:
        error_msg = f"[ERROR] [{current_datetime}]: ValueError msg in line {sys.exc_info()[2].tb_lineno},"
        logging.error(error_msg)
        print("\n")

    if choice == "3":
        n = 1
        students = sms.list_student()
        if len(students) == 0:
            print("学生列表为空，请添加学生信息")
        else:
            for student in students:
                print(student)
        print("\n")
    try:
        if choice == "4":
            n = 1
            ID = int(input("请输入要查询的学生的ID："))
            if sms.sercher_student(ID):
                print("查询成功")
            else:
                print("未查找到该学生")
            print("\n")
    except:
        error_msg = f"[ERROR] [{current_datetime}]: ValueError msg in line {sys.exc_info()[2].tb_lineno},"
        logging.error(error_msg)
        print("请输入正确的ID")
        print("\n")
    if n == 0:
        print("请输入正确的选择")
        print("\n")
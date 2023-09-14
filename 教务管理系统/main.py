from operator_module import *
import logging

logging.basicConfig(filename='student_management.log', level=logging.ERROR)

if __name__ == "__main__":
    while 1:
        print("学生管理系统")
        print("1.添加学生")
        print("2.删除学生")
        print("3.列出学生")
        print("4.查询学生")
        print("5.退出")
        choice = input("请选择操作：")
        if choice == "5":
            break
        operate(choice)
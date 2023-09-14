from operator_module import *
x=None
y=None
while(1):
    if __name__ == "__main__":
        operation = input("请输入要进行的计算类型：加/减/乘/除/模（要结束程序请输入end）：")
        if operation == "end":
            break
        
        try:
            x = float(input("请输入第一个数字："))
            y = float(input("请输入第二个数字："))
            result = calculator(operation,a,y)
            print("计算结果为" + str(result) + "\n")

        except ValueError as e:
            current_datetime = datetime.datetime.now()
            error_msg = f"[ERROR] [{current_datetime}]: ValueError msg in line {sys.exc_info()[2].tb_lineno}, {str(e)}"
            logging.error(error_msg)
        
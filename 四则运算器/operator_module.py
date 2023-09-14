import sys
import logging
import datetime

def add(x,y):
    '''
    @param x:
        addend
    @param y:
        addend
    @return:
        sum of two numbers
    @test
    >>> add(1,2)
    3
    '''
    return x + y

def sub(x,y):
    '''
    @param x:
        suntraction
    @param y:
        suntraction
    @return:
        diffrernce of two numbers
    @test
    >>> sub(5,3)
    2
    '''
    return x - y

def mul(x,y):
    '''
    @param x:
        multiplier
    @param y:
        multiplier
    @return:
        product of two numbers
    @test
    >>> mul(5,6)
    30
    '''
    return x * y

def div(x,y):
    '''
    @param x:
        dividend
    @param y:
        divisor
    @return:
        quotient of two numbers
    @test
    >>> div(6,3)
    2.0
    '''
    if y == 0:
        raise ValueError("除数不能为0")
    return x / y

def mod(x,y):
    '''
    @param x:
        dividend
    @param y:
        divisor
    @return:
        the remainder of quotient of two numbers
    @test
    >>> mod(8,3)
    2
    '''
    if y == 0:
        raise ValueError("除数不能为0")
    return x % y

def calculator(operation,x,y):
    """
    @param:
        calculator main function
    """
    try:
        if operation == "加":
            return add(x,y)
        elif operation == "减":
            return sub(x,y)
        elif operation == "乘":
            return mul(x,y)
        elif operation == "除":
            return div(x,y)
        elif operation == "模":
            return mod(x,y)
        else:
            raise TypeError("请输入加/减/乘/除/模等操作")
        
    except ValueError as e:
        current_datetime = datetime.datetime.now()
        error_msg = f"[ERROR] [{current_datetime}]: ValueError msg in line {sys.exc_info()[2].tb_lineno}, {str(e)}"
        logging.error(error_msg)
    except TypeError as e:
        current_datetime = datetime.datetime.now()
        error_msg = f"[ERROR] [{current_datetime}]: TypeError msg in line {sys.exc_info()[2].tb_lineno}, {str(e)}"
        logging.error(error_msg)



###########################
# Decorator example #0
###########################
def add_pattern(func):
    # adds a pattern while printing a function output
    # decorator function returns a wrapper function as a variable
    def wrapper():
        print("-----------------------------------------")
        func()
        print(" ")
    return wrapper


###########################
# Decorator example #1
###########################
def welcome(func):
    def wrapper():
        print("Performing", end=' ')
        func()
    return wrapper

@welcome
def addition():
    print("Task 1")

@welcome
def subtraction():
    print("Task 2")

@add_pattern
def example_1():
    print("Example 1")
    addition()
    subtraction()


###########################
# Decorator example #2
###########################
import numpy as np

def calculator(func):
    # decorator function returns a wrapper function as a variable
    def wrapper():
        arr_val = func()
        print(arr_val)
        print("Sum = ", np.sum(arr_val))
        print("First Order Difference = ", np.diff(arr_val))
        print("Product = " ,np.prod(arr_val))
    return wrapper

@calculator
def get_num():
    print("Performing array math on ", end='')
    arr_val = np.ceil(np.random.rand(10)*10)
    return arr_val

@add_pattern
def example_2():
    print("Example 2")
    get_num()


###########################
# Decorator example #3
###########################
from datetime import datetime
def logger(func):
    # function that logs function usage
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write(f'''Called function {func.__name__} with args [{" ".join([str(arg) for arg in args])}] at {str(datetime.now())} \n''')
        func(*args, **kwargs)
    return wrapper

@logger
def get_str(str_val1, str_val2="world"):
    print(str_val1, str_val2)

@add_pattern
@logger
def example_3():
    print("Example 3")
    get_str("hello")


def main():
    example_1()
    example_2()
    example_3()


if __name__=="__main__":
    main()
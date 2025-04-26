# import sys


# # print(dir(sys))  #what are function or action which is stored inside the module

# # print(sys.builtin_module_names)  #what are the inbuilt modules have in python

# import math  #python inbuilt library

# print(math.sqrt(144))
# print(dir(math))

# import pandas   #opensource library numpy , matplotlib and seaborn

# print(dir(pandas))

# #function :  function are block of reusable code that performs specific task

# #syntax  #user-define fucnctions

# # def function_name(parameter):
# #     return result

def greet(name):
    print(f"Hello, {name}")

greet("Satyam")


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def divide(a,b):
    return a/b

def floorediv(a,b):
    return a//b

def modulus(a,b):
    return a%b

def exponent(a,b):
    return a**b



print(add(10,100))
print(sub(100,10))
print(multi(10,100))
print(divide(10,100))
print(floorediv(10,100))
print(modulus(10,100))
print(exponent(10,100))

#Task_1

def factorial(number):
    num=1
    while number>=1:
        num=num*number
        number=number-1
    return num
result=int(input("Enter a number: "))
print(f"Factorial of {result} is:  {factorial(result)} ")


#Task_2
choice=float(input("Enter a number: "))
import math
squareroot=math.sqrt(choice)
log=math.log(choice)
sine=math.sin(choice)
print(f"Square root: {squareroot} ")
print(f"logarithm: {log} ")
print(f"sine: {sine} ")

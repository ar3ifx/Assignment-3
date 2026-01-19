def factorial(number):
    num=1
    while number>=1:
        num=num*number
        number=number-1
    return num
result=int(input("Enter a number: "))
print(f"Factorial of {result} is:  {factorial(result)} ")



# Write a program to find a factorial of a number.

def factorial(num):
    if (num==0 or num==1):
        return 1
    else:
        return num*factorial(num-1)
n=7
f=print("factorial of number is :",factorial(n))
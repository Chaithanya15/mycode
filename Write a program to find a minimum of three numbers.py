# Write a program to find a minimum of three numbers.

         
number1=int(input("enter num1:"))
number2=int(input("enter num2:"))
number3=int(input("enter num3:"))

if number1<number2 and number1<number3:
    print("num1 is minimum")
if  number2<number3 and number2<number1:
    print("num2 is minimum")
if number3<number1 and number3<number2 :
    print("num3 is minimum")

def Primechecking(num):
    if num>1 :
        for i in range(2,int(num/2)+1):
            if(num% i) == 0:
                print("the number ", num,"is not a prime num")
                break
        else:
            print("the number ", num,"is not a prime num")
    else:

        print("num",num,"is not prime num")

num = int(input("Enter a number to check prime or not: "))  
# To print the result, whether a given number is prime or not  
Primechecking(num)  
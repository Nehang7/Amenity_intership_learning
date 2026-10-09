def factorial(num):
        if ( num==0 or num==1):
            return 1
        else:
            return (num * factorial(num-1))
 
num=int(input("enter number to find factorial : " ))
print("Number",num)
print ("Factorial",factorial(num))



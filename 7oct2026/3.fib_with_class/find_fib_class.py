
class fibbonaci:
    def fib(self,n):
        if n==0:
            return 0
        elif(n==1):
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
 

f = fibbonaci()
n=int(input("enter number to find fib" ))
result=f.fib(n)
print(f"value of fib {n} is {result}")



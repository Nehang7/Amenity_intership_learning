n=int(input("enter number "))
m=int(input("enter number "))

for i in range(n+1):
    for j in range(m+1):
        if j>=i and j<=m-i:
         print("*",end='')
        else :
            print(" ",end='')
    print()
            
        


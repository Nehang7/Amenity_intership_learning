n =int(input("enter nnumber to print pattern : "))

for i in range(1,n+1): #loop run unitl the the enter variable
    for j in range(1,n+1):
        if j<=i:
            print("*",end='')
        else :
            print(" ",end='')
    print()
            
        

a = int(input("enter the value of n:"))
nsp = a+1
for i in range(1,a+1):
    for j in range (1,i+1):
        print("*",end="")
    for k in range(1,nsp+1):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    nsp = nsp-2
    print()
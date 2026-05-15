#     *
#    * *
#   *   *
#  *     *
# *********
# print this pattern

a = int(input("enter positive num.:"))
nsp = 2
for i in range(1,a+1):
    if i ==a:
        for i in range(1,2*i):
            print("*",end="")
    else:
        for j in range(a,i,-1):
            print(" ",end="")
        for k in range(1,nsp):
            if k==1 or k==nsp-1:
                print("*",end="")
            else:
                print(" ",end="")
        nsp+=2
    print()
    
print("DHIRAJ JUNGHARE")
num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:
        flag = False
        break
print("Prime" if flag and num > 1 else "Not Prime")
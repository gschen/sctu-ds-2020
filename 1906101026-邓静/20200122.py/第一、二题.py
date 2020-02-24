#求给定数的阶乘
def H(n):
    error_num = [1,10,20,30,40,50]
    if n == 0 or n == 1:
        return 1
    if n in error_num:
        return "错误"
    else:
        return n*H(n-1)
a=H(5)
print(a)


#单利公式
import math
P=int(input("p=:"))
R=int(input("G=:"))
T=int(input("T=:"))
Q=(P*R*T)/100
print(Q)
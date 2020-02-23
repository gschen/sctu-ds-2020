#1、求给定数的阶乘 要求：所求阶乘不可以是这几个数：[1,10,20,30,40,50]
list1=[1,10,20,30,40,50]
def factorial(n):
    if n ==1:
        return 0
    else:
        return (n*factorial(n-1))
while True:  
    m=int(input())
    if m<0 or m in list1:
        break9
    else:
        print(factorial(m))
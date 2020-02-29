"""
6.	（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""
a = 1
b = 2
c = 1
sum = 0
x = int(input())
def N(x):
    global a,b,c,sum
    if x % 2 == 0:
        for i in range(x):
            sum = a/b + sum
            a,b = a,b*2
    else:
        for i in range(x):
            sum = a/c + sum
            a,c = a,c+2
    return sum
print(N(x))
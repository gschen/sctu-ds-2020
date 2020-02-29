#求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定。

list=[14,25,98,75,23,1,4,56,59]
n=int(input("输入一个整数n:"))
x=len(list)
if n>x or n<1:
    print("不满足要求")
else:
    s=0
    while n>=1:
        s+=list[n-1]**2
        n=n-1
    print(s)
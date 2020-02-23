#4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定。
list=[14,25,98,75,23,1,4,56,59]
n=int(input())
sum=0
if n>9:
    print("输入错误")
else:
    for m in range(n):
        sum = sum+list[m]**2
    print(sum)
#求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定。

list0=[14,25,98,75,23,1,4,56,59]
x=int(input())
if 1<=x<=9:
    sum=0
    for y in list0[:x]:
        sum=sum+y*y
    print(sum)
else:
    print("输入有误!")   
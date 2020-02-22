#求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定。


list1=[14,25,98,75,23,1,4,56,59]
n=int(input())
if 1<=n<=9:
    sum=0
    for m in list1[:n]:
        sum=sum+m*m
    print(sum)
else:
    print("输入有误！")
# 4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
# 要求：n需要是input输入，且小于数组长度，不能固定。
list=[14,25,98,75,23,1,4,56,59]
n=int(input('输入前所要求的的n个数:'))
if n>=1 and n<=9:
    sum=0
    for a in list[:n]:
        sum=sum+a*a
    print(sum)
else:
    print("错误")
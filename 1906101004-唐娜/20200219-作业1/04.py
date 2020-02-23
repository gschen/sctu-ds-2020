#4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定。

n = int(input('请输入一个整数：'))
x = [14,25,98,75,23,1,4,56,59]
s=len(x)
sum=0
if n >= s:
    print('超出范围')
else:
    for i in s[:n]:
        sum=sum+i**2
print(sum)
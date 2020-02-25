#求数组中前N个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求n需要是input输入，且小于数组长度，不能固定
n=int(input('请放入一个整数：'))
x=[14,25,98,75,23,1,4,56,59]
a=len(x)
sum=0
if n >= a:
    print('error')
else:
    for i in x[:n]:
        sum=sum+i**2
print(sum)
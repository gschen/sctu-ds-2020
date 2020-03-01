#4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定。
list=[14,25,98,75,23,1,4,56,59]
n=int(input('请输入一个数：'))
sum=0
if 1<=n<=9:
    for x in list[:n]:
        sum=sum+x**2
    print(sum)
else:
    print('输入错误')

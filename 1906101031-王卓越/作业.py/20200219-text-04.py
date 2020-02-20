# 4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
# 要求：n需要是input输入，且小于数组长度，不能固定。
li=[14,25,98,75,23,1,4,56,59]
n=int(input())
sum=0
if n<len(li):
    for x in li[:n]:
        sum=sum+x**2
    print(sum)
else:
    print('n超过了数组的长度')



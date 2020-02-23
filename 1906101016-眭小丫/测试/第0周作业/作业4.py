list1=[14,25,98,75,23,1,4,56,59]
p=len(list1)
print('列表的长度为%d' % len(list1))
n=int(input('请输入一个0到9的整数：'))
if 0<n<=p:
    sum=0
    for m in list1[:n]:
        sum=sum+m*m
        print(sum)
else:
    print('False')



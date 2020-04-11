#第 一题
wrong_list=[1,10,20,30,40,50]
n=int(input('请输入n='))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
if n in wrong_list:
    print('请输入别的数字')
else:
    print(fact(n))


#第二题
P=int(input('输入：P='))
R=int(input('R='))
T=int(input('T='))
s=(P*R*T)/100
print('输出：%d'%(s))


#第三题
lis1=[14,25,98,75,23,1,4,56,59]
max1=max(lis1)
print("最大值是:%d"%max1)


#第四题
lis1=[14,25,98,75,23,1,4,56,59]
n=int(input('请输入整数：'))
lisn=lis1[:n]
def mei(*lisn):
    r=0
    for i in lisn:
        r=r+(i**2)
    return r
print(mei(*lisn))


#第五题
lis=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split(','))
numa=lis[a]
numb=lis[b]
lis[a]=numb
lis[b]=numa
print(lis)

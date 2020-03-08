#第一题
def jiecheng(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*jiecheng(n-1)
    print(jiecheng(6))

    #第二题
def danli()
    p=input('请输入本金p:')
    t=input('请输入时间t:')
    r=input('请输入利率r:')
    c=float((float(p)*float(t)*float(r))/100)
    print('单利是:%d'%(c))
danli()

#第三题
max_num = max([14,25,98,75,23,1,4,56,59])
print(max_num)

#第四题
n = int(input())
list1 = [14,25,98,75,23,1,4,56,59]
list_result = []
lenth = len(list)

if n > lenth:
    print('error') 
else:
    for i in range(n)
        list_result.append(list1[i]**2)
    result = sum(list_result)
print(result)

#第五题
lis=[14,25,98,75,23,1,4,56,59]
x,y=map(int,input('请输入两个数').split())
lis[x],lis[y] = lis[y],lis[x]
print(lis)

def f(x):
    if x == 0:
     return 0
    eilf x == 1:
    return 1
    else:
        return (x * f(x-1))
print (f(5))


#第二题

def x()：
    p=input('请输入本金p:')
    t=input('请输入时间t:')
    r=input('请输入利率r:')
    c=float((float(p)*float(t)*float(r))/100)
 print('单利是:%d'%(c))


 #第三题

 list1 = [14,25,98,75,23,1,4,56,59]
 print(max(list1))

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

list=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split())
list[a],list[b]=list[b],list[a]
print(list
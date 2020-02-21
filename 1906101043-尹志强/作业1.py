# coding=utf-8
#第一题
while True:
    a=eval(input('请输入一个正整数：'))
    if a in [1,10,20,30,40,50]:
        print('不能是，1，10，20，30，40，50')
    else:
        b=a
        for y in range(1,a):
            b=b*y
        print('它的阶乘为：%s'%(b))
        break



#第二题
P,T,R=eval(input('请依次输入本金P，时间T，和利润R,中间用‘，’隔开：'))
a=P*T*R/100
print('单利是：%s'%(a))


#第三题
list1=[14,25,98,75,23,1,4,56,59]
a=0
for x in list1:
    if x>a:
        a=x
    else:
        a=a
print("最大值是:%d"%(a))


#第四题
list2=[14,25,98,75,23,1,4,56,59]
while True:
    n=eval(input('请输入你要求数组前n的平方和n的值：'))
    if n>len(list2):
        print('没有这么多个数')
    else:
        g,f=0,1
        while n>=f:
            g=g+list2[n-1]**2
            n=n-1
        print(g)
        break


    #第五题
    import random
    list3=[14,25,98,75,23,1,4,56,59]
    list4=random.sample(range(0,len(list3)),2)
    a,b=int(list4[0]),int(list4[1])
    list3[a],list3[b]=list3[b],list3[a]
    print(a,b)


    
    








            
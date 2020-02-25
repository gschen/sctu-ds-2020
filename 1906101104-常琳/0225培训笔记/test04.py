#用for循环找出列表中元素的最大值：
list1=[1,2,6,8,3]
a=list1[0]
for i in list1:
    if i>a:
        a=i
print(a)

#计算列表中数值之和：(isinstance)
print(isinstance(1,int))
list2=[1,2,5,4,'a']
sum=0
for i in list2:
    if isinstance(i,int):
        sum+=i
print(sum)

#判断6是否是素数：
n=6
for i in range(2,n):
    if n%i==0:
        print('不是素数')
        break
    else:
        print('是素数')

#判断2-n之间有多少个素数;
n=int(input('输入n的值：'))
sum=0
for i in range(2,n+1):
    for j in range(2,i):
        if i % j ==0:
            break
        else:
            sum+=1
print(sum)



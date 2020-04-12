
a={'a','c','v','v',1}
b=(set('zwsa'))

print(a|b)  #并集
print(a-b)  #补集 
print(a&b)   #交集
print(a^b)   #不同时包含
a.add('q')  #添加元素，但加入相同不重复
print(a)
b.update({1,2},[4,3],'l')  #元素添加可以是列表，元组，str
print(b)  
a.remove('c')  #删除元素，如果列表无此元素就报错
print(a)
a.discard('d')   #删除元素，无此元素也不会报错
print(a)
a.pop() #s随机删除  
print(a)
  

字典
dic={'name':'zhanshan','age':19,'school':'qhinghua'}
print(dic)
xiu gaishuju
dic['name']='lisi'
print(dic)

#查找数据

dic.get('name')
print(dic)
dic.setdefault('name')
print(dic)

#tianj添加数据
#dic['class']='class one'
#print(dic)


#删除数据
#del dic['name']
#print(dic)

#dic.pop('name')
#print(dic)


#dic.popitem()
#print(dic)



age=int(input('请输入n年龄：'))
if age >=18:
    print('adult')
else :
    print('kid')



n1=25
n2=20
while (n1!=n2):  
    n2=int(input('shurushuzi:'))
if n1>n2




num = int(input('输入数字:'))
if num%2==0:
    if num % 3 == 0 :
        print('2.3都能别整除')  
else:
    if num % 3 == 0:
        print('3can,2 no can ')
    else:
        print('2,3 都不可以')






count=0

while count<=5:
    print(str(count),'<5')
    count=count+1
else:
    print(str(count)+'5')




list1=[1,2,3,4,5]
for i in list1:
    print(i)

str1='abcdefg'
for j in str1:
    print(j)


for i in range(6):
    print(i)

for i in range(0,11,5):
    print(i)




list(range(5))
print(list(range(5)))



list=[1,2,3,2]
a=list[0]
for i in list:
    if i >a:
        a=i
print(a)




# list=[1,2,3,2]
# a=list[0]
# for i in list:
#     if i >a:
#         a=i
# print(a)


# print(isinstance(1,int))


# list2=[1,2,3,4,'a,',1]
# sum=0
# for i in list2:
#     if isinstance(i,int):
#         sum =sum+i  
# print(sum)  



# x=13
# for i in range(2,x):   
#     if x%i==0:
#         print('不是素数')
#         break
#     else:
#         print('是素数')



x=5
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i%j==0:
            break

    else:
       sum=sum+1
print(sum)



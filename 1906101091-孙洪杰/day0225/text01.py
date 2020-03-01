#集合
A={'a','b','c','c',1}#集合具有元素的唯一性
# B=set('aabbcc')#set返回的是一个集合
# print(A,B)

 #补集
# print(A-B)

 #并集
# print(A|B)

 #交集
# print(A&B)

 #不同时的包含
# print(A^B)

 #增加元素
# A.add('k')
# A.update({1,3},[4,2],'e')
# print(A)

#删除元素
# A.pop()#集合中的pop随机删除元素
# # A.remove('b')
# # A.discard('k')#即使元素不存在于集合，也不会报错
# print(A)

#字典
dic={'name':'张三','age':'19','sex':'男'}
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# for x in dic:
#     print('{}:{}'.format(x,dic[x]),end='')
# print('')
print(dic.get('id'))
dic['id']=5
print(dic)
#删除数据
del dic['id']
dic.pop('name')
dic.popitem()#随即返回并删除一对键值对
print(dic)

#条件判断
# age=int(input())
# if age >= 18:
#     print('你已经成年了')
# else:
#     print('你个小鬼')

# #猜大小
# num1=25
# num2=1
# while (num1!=num2):
#     num2 = int(input('请猜一个数字:'))
#     if num1>num2:
#         print('猜小了')
#     if num2>num1:
#         print('猜大了')
#     if num2==num1:
#         print('猜测对了')

# #判断能不能整除
# num = int(input("请输入一个数字:"))
# if num % 2==0:
#     if num % 3==0:
#         print('这个数既能被2整除，又能被3整除')
# else:
#     if num % 3==0:
#         print('这个数不能被2整除，能被3整除')
#     else:
#         print('这个数不能被2整除也不能被3整除')

#循环
#while 求0-100的和
# sum=0
# a=1
# while (a<=100):
#     sum+=a
#     a+=1
# print(sum)

# #while 无限循环
# while True:
#     print('无限循环')

# count=0
# while count<5:
#     print('{}<{}'.format(count,5))
#     count+=1

#for 循环
strs='abcdefg'
for i in range(1,6):
    print(i,end=' ')
print(' ')

for i in strs:
    print(i,end=' ')
print(' ')

for i in range(1,20,2):
    print(i,end=' ')
print(' ')

print(list(range(5)))

#课堂小练习
lis=[1,2,2,3,2,4]
a=lis[0]
for i in lis:
    if i>a:
        a=i
print(a)

li=[1,2,3,'a',1]
sum=0
for i in li:
    if isinstance(i,int):
        sum+=i
print(sum)
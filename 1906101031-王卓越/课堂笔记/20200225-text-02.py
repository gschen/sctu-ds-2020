# #条件判断
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


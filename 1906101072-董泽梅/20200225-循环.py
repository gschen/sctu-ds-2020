#01
#age=int(input('请输入你的年龄'))
#if age>=18:
#	print('您已经成年啦')
#else:
#	print('您还未成年')

#num = 25
#num2 = 1
#while (num !=num2):
#    num2 = int(input('请输入你猜的数据'))
#    if num > num2:
#        print('你输入的值太小了')
#    elif num < num2:
#        print('你输入的值太大了')
#    else:
#        print('猜对了')


#02
#num = int(input("请输入一个数字"))
#if num % 2 ==0:
#    if num % 3 == 0:
#        print("这个数字既能被2整除，也能被3整除")
#    else:
#        print("这个数字可以被2整除，不能被3整除")
#else:
#    if num % 3== 0:
#        print("这个数字可以被3整除，不能被2整除")
#    else:
#        print("这个数既不能被2整除也不能被3整除")


#03
#1到100的和
# sum = 0
# a = 1
# while (a <= 100):
#     sum = sum + a
#     a = a+1
# print(sum)

#无限循环
#while(a<=100):
#	print("无限循环！！！")


#while循环
# count = 0
# while count < 5:
#     print(str(count),"< 5")
#     count=count+1
# else:
#     print(str(count)+"=5")

#for循环
#list1=[1,2,3,4,5]
#for i in list1:
#	print(i)

#str='abcdefg'
#for j in str:
#	print(j)

#range
#for i in range(5):
#	print(i)

#for i in range(2,10):
#	print(i)

#for i in range(0,11,2):
#	print(i)

#print(list(range(5)))

#循环小练习
#找出列表中最大元素

# list = [1,2,3,4]
# a = list[0]
# for i in list:
#     if i > a:
#         a=i
# print(a)

#列表数之和

# list = [1,2,3,4,'a',5]
# sum = 0
# for i in list:
#     if isinstance(i,int):
#         sum = sum+i
# print(sum)

#输入n，检查2到n之间有多少素数

# x = int(input())
# for i in range(2,x):
#     if x % i ==0:
#         print("不是素数")
#         break
# else:
#     print("是素数")

# x = 5
# sum = 0
# for i in range(2,x+1):
#     for j in range(2,i):
#         if i %j == 0:
#             break
#     else:
#         sum = sum+1
# print(sum)


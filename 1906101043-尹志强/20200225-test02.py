# age=int(input('请输入你的年龄'))
# if age >=18:
#     print('你已经成年了')
# else:
#     print('你还未成年')





# #2
# num1=25
# num2=1
# while(num1 != num2):
#     num2 = int(input('请输入你猜的数字：'))
#     if num1 > num2:
#         print('你输入的值小了')
#     elif num1 < num2:
#         print('你输入的值大了')
# print('猜对了')





# #3
# num = int(input('亲输入一个数字：'))
# if num % 2==0:
#     if num % 3 == 0:
#         print('这个数既能被2整除也能被3整除')
#     else:
#         print("这个数能被2整除，不能被3整除")
# else:
#     if num%3==0:
#         print('这个数可以被3整除，不能被2整除')
#     else:
#         print('既不能被3整除，也不能被2整除')

# #4
# sum=0
# a=1
# while(a<=100):
#     sum=sum+a
#     a=a+1
# print(sum)


##5
# while():
#     print('无限循环中！！！')


# #6
# count=0
# while count<5:
#     print(str(count),'<5')
#     count=count+1
# else:
#     print(str(count)+"=5")



# #7
# list1=[1,2,3,4,5,6]
#  for i in list1:
#      print(i)


# str1='abcde'
# for j in str1:
#     print(j)





#8
# for i in range(5):
#     print(i)


# for i in range(0,11,3):#(3代表隔开几个)
#     print(i)


# print(list(range(5)))

# list1=[1,5,6,2]
# a=list1[0]
# for i in list1:
#     if i>a:
#         a=i
# print(a)




# #9
# list2=[1,2,3,4,5,'a']
# sum=0
# for i in list2:
#     if isinstance(i,int):
#         sum=sum+1
# print(sum)



# n=eval(input('请输入一个数：'))
# for i in range(2,n):
#     if n%i==0:
#         print('不是素数')
#         break
# else:
#     print('是素数')


# for i in range(2,11):
#     for j in range(2,10):
#         if i%j ==0:
#             print('不是素数')
#         else:
#             print('是素数')








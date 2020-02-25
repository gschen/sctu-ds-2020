# age = int(input('请输入你的年龄：'))
# if age >= 18:
#     print('你已成年')
# else:
#     print('你未成年')


#猜数字
# num1 = 25
# num2 = 1
# while(num1 != num2):
#     num2 = int(input('请输入你猜的数字：'))
#     if num1 > num2:
#         print('你输入的值太小')
#     elif num1 < num2:
#         print('你输入的值太大')
# print('猜对了')


# 整除
# num = int(input('请输入一个数字：'))
# if num & 2 == 0:
#     if num % 3 == 0:
#         print('这个数字能被2和3整除')
#     else:
#         print('这个数字能被2整除')
# else:
#     if num % 3 == 0:
#         print('这个数字能被3整除')
#     else:
#         print('这个数字既不能被3整除也不能被2整除')

 
# while语句
# sum = 0
# a = 1
# while a <= 100:
#     sum += a
#     a +=1
# print(sum)

# while True:
#     print('无限循环')


# cnt = 0
# while cnt < 5:
#     print(str(cnt),'<5')
#     cnt += 1
# print(cnt,'=5')



# for循环
# list1 = [1,2,3,4,5]
# for i in list1:
#     print(i)

# str1 = 'abcdefg'
# for j in str1:
#     print(j)

# for i in range(5):
#     print(i)

# for i in range(0,20,2):
#     print(i)

# print(list(range(5)))

# 练习：
# 1、找最大值
# list1 = [1,2,3,4]
# a = 0
# for i in list1:
#     if i > a:
#         a = i
# print(a)

# 2、找出数值求和
# list2 = [1,2,3,'a']
# sum = 0
# for i in list2:
#     if isinstance(i,int):   # isinstance()函数用来判断一个对象是否是一个已知的类型，类似type()
#         sum += i
# print(sum)

# 3、素数
# x = 5
# for i in range(2,x):
#     if x % i == 0:
#         print('不是素数')
#         break
# else:
#     print('是素数')

# 素数个数
# x = 10
# sum = 0
# for i in range(2,x+1):   
#     for j in range(2,i):  
#         if i % j == 0:
#             break
#     else:
#         sum += 1
# print(sum)



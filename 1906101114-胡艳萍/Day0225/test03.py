# 练习：

# 1、找最大值
# list1=[1,2,3,4]
# a=0
# for i in list1:
#     if i>a:
#         a=i
# print(a)


# 2、数值的求和
# list2=[1,2,3,4,'a',1]
# sum=0
# for i in list2:
#     if isinstance(i,int):     # isinstance()函数用来判断一个对象是否是一个已知的类型，类似type()
#         sum+=i
# print(sum)

# 3、判断是否为素数
# x=5
# for i in range(2,x):
#     if x%i==0:
#         print('不是素数')
#         break
# else:
#     print('是素数')

# 4、求素数的个数
# x=10
# sum=0
# for i in range(2,x+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:sum+=1
# print(sum)

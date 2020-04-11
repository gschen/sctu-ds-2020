# 1、给定一个列表,找列表中最大的元素
# 输入：[1,2,3,2]
# 输出：3

# list=[1,2,3,2]
# print(max(list))

# list=[1,2,3,2,6,10,1]
# a=list[0]
# for i in list:
#     if i>a:
#         a=i
# print(a)


# 2、计算列表中数字之和
# 输入：[1,2,3,"a",1]
# 输出：7

# list=[1,2,3,"a",1]
# sum=0
# for i in list:
#     if isinstance(i,int):  #isinstance() 函数来判断一个对象是否是一个已知的类型
#         sum=sum+1
# print(sum)


# 3、输入n，检查2-n之间有多少个素数（质数是大于1（不包括1）的自然数，除1及其本身外，没有除数。）
# 输入：5
# 输出：3
# 原因：1-5，素数有2，3，5

# x=4
# for i in range (2,x):
#     if x%i==0:   # “=”表赋值，“==”表判断，判断两个是否一样相等
#         print("不是素数")
#         break
# else:
#     print("是素数")


x=7
sum=0
for i in range(2,x+1):
    for j in range(2,7+1):
        if i%j==0:
            break
    else:
        sum=sum+1
print(sum)
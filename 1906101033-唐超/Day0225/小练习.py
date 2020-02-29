# 1.给定一个列表,找列表中最大的元素
#   输入: [1,2,3,2]
#   输出: 3

list = [1,2,3,2]

a  = list[0]

for i in list:
    if i > a:
        a=i
print(a)





# 2、计算列表中数字之和
# 输入: [1,2,3,"a",1,'b',21]
# 输出: 7
list1 = [1,2,3,4,'a',1,'b',21]

sum = 0

for i in list1:
    if isinstance(i,int):
        sum = sum + i
print(sum)

# 3、输入n，检查2-n之间有多少个素数(质
# 数是大于1 (不包括1)的自然数，除1及其.
# 本身外，没有除数。)
# 输入: 5
# 输出: 3
# 原因: 1-5， 素数有2，3，5
x = int(input('请输入一个数'))
for i in range(2,x):
    if x % i == 0:
        print('不是素数')
        break
else:
    print('是素数')

x = 10

# for i in range(2,x+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         sum = sum + 1
# print(sum)

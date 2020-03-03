# 1、给定一个列表，找列表中最大元素
#    输入：[1,2,3,2]
#    输出：3
list = [1,2,3,2]
a = list[0]
for i in list:
    if i > a:
        a = i
print(a)

# 2、计算列表中数字之和
#    输入：[1,2,3,'a',1]
#    输出：7
list1 = [1,2,3,'a',1]
sum = 0
for i in list1:
    if isinstance(i,int):
        sum = sum + i
print(sum)

# 3、判断输入的数是不是素数
n = int(input('输入一个数：'))
for i in range(2,n):
    if n % i == 0:
        print('不是素数')
        break
else:
     print('是素数')

# 4、输入n，检查2-n之间有多少个素数
#    输入：5
#    输出：3
n = int(input())
sum =0
for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum +1
print(sum)


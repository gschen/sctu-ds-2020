#x小练习

#给定一个列表，找最大数
# list1 = [1,2,3,2,5,10]
# a = list1[0]

# for i in list1:
#     if i > a:
#         a=i
# print(a)


#计算列表数字之和
list2 = [1,2,3,4,'a',1]
sum = 0
for j in list2:
    if isinstance(j,int):
        sum = sum + j
print(sum)



#检查给定数是否为素数
x = 5
for k in range(1,x):
    if x % k== 0:
        print('不是素数')
        break
else:
    print('是素数')



#输入n，检查2-n之间有多少个素数   输入5
x=5
sum = 0 
for h in range(2,x+1):
    for n in range(2,h):
        if h % n == 0:
            break# 不是素数，跳出循环
    else:
        sum = sum + 1
    print(sum)
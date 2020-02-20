# 1、求给定数的阶乘
n = eval(input('请输入一个数:'))
m = 1
for i in range(1,n+1):
    m = m*i
print(m)


# 2、求单利
p = eval(input('请输入本金:'))
t = eval(input('请输入时间:'))
r = eval(input('请输入利率:'))
dl = (p*t*r)/100
print(dl)

# 3、查找数组中的最大元素
l =  [14,25,98,75,23,14,56,59]
print(max(l))


# 4、求前n个数的平方和
n = eval(input('请输入一个数:'))
L0 = [14,25,98,75,23,14,56,59]
L1 = L0[0:n]
sum = 0
for x in (L1):
    sum+=x*x
print(sum)


# 5、交换列表中的任意两个元素
L2 = [14,25,98,75,23,14,56,59]      #默认列表第一个元素的位置为0
t = int(input('请输入要替换的位置:'))
s = int(input('请输入要替换的位置:'))
L2[t],L2[s] = L2[s],L2[t]
print(L2)
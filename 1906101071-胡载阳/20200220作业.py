# 1
'''
l = [1,10,20,30,40,50]
def num(x):
    if x == 0:
        return 1
    else:
        return x*num(x-1)
x = int(input())
if x in l:
    print('not number')
else:
    print(num(x))
'''

# 2
P = int(input('输入本金：'))
R = int(input('输入利率：'))
T = int(input('输入时间：'))
s = (P * T * R) / 100
print(s)


# 3
def serch_max():
    list = [14, 25, 98, 75, 23, 1, 4, 56, 59]
    i = max(list)
    return i


# 4
lis = [14, 25, 98, 75, 23, 1, 4, 56, 59]
n = int(input())
s = 0
for i in range(n):
    s += lis[i] ** 2
    print(s)

# 5
list = [14, 25, 98, 75, 21, 1, 4, 56, 59]
n = int(input('请输入要交换的第一个数：'))
m = int(input('请输入要交换的第二个数：'))
n = list.index(n)
m = list.index(m)
list[n], list[m] = list[m], list[n]
print(list)
#字符串连接

a='hi'
b='s'
print(a+b)

#重复输出字符串

c='hi'
print(c*3)

#通过索引获取字符串中字符

str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])

#格式化字符串与格式化整数

print('我叫%s' % ('张三'))
print('我今年%d'%(18))

#列表函数
list=[5,4,2,8,3,8]
list.append(7)
print(list)
list.extend([1,2])
print(list)
list.sort()
print(list)
list1=[1,2,3,[4,5,6]]
print(len(list1))
for x in range(len(list1)):
    print(list[x])

#元组
tup1 = ('Google', 'Runoob', 1997, 2000)
#tup1[1]='tangdi'
print(tup1)
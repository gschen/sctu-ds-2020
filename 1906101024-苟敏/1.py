#链接字符
a="hi"
b="s"
print(a+b)

#切片
str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])

#格式化输出
print('我的名字是%s'%('lrb'))
print('我今年%d'%('18'))

#列表
list=[1,2,3,[4,5,6]]
print(len(list))
for x in range(len(list)):
    print(list[x])

list=[1,2,3,[4,5,6]]
list.append(7)
list.extend([1,2])
print(list)

#添加
list=[1,3,[4,5,6]]
list.append(7)
list.extend([1,2])
print(list)

#索引
list=[1,3,4,5,6]
print(list.index(3))

#排序
list.sort()
print(list)

#元组
tup=('s',20,[5,9])
tup[1]=200
print(tup)
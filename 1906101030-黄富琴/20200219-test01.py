a='hi'
b='s'
print(a+b)

c='hi'
print(c*3)

str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])

#格式化输出
print("我叫%s"%('张三'))
print("我今年%d"%(10))

#列表
list=[1,2,3,[4,5,6]]
print(len(list))
for x in range(len(list)):
    print(list[x])

#添加
list=[5,4,2,8,3,8]
list.append(7)
list.extend([1,2])
list.pop()

#排序
list.sort()
print(list)

#元组
tup=('s',100,[1,2])
tup[1]-200
print(tup)
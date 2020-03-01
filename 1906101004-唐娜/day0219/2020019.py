#连接字符
a='hi'
b='s'
print(a+b)


#重复字符
c='hi'
print(c*3)


#切片
str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])


#格式化输出
print("我叫%s"%('张三'))
print("我今年%d"%(10))

#列表
list1=[1,2,3,[4,5,6]]
print(len(list1))
for x in range(len(list1)):
    print(list1)

lis1=[1,2,3,[4,5,6]]
list1.pop(2)
list1.append(7)
list1.extend([1,2])
print(list1)
print(list1.index(2))


list2=[5,4,2,8,3,8]
list2.sort()
print(list2)


#元组  元素不限但不可更改
tup=('s',100,[1,2])
print(tup)


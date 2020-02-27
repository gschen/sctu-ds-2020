
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
print('b' in str1)
print('v' not in str1)

#格式化输出
print("我叫%s"%('张三'))
print("我今年%d"%(10))

#列表
list=[5,4,2,8,3,8]
list.append(7)
list.extend([1,2])
list.pop(1)
list.sort()
print(list)
list2=[5,8,6,4,2,5,8,9,1]
list2.sort()
print(list2)
# sorted有返回值，sort没有返回值

#元组
tup=('s',100,[1,2])
# tup[1]=200  元组元素不能被更改
print(tup)
tup[2][1]=3
print(tup)
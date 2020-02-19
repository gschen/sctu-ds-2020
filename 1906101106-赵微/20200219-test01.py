a='hi'
b='s'
print(a+b)


#重复字符

c='hi'
print(c*3)

str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])

#格式化输出
print("我叫%s"%('百分号占位符'))
print("我今年%d岁嘞"%(10))

#列表
list=[1,2,3,[4,5,6]]
print(len(list))

for x in range(len(list)):
    print(list[x])

list.append(7)
list.extend([1,2])
list.pop()
list=list.sort
print(list)

#元组
tup=('s',100,[1,2])
tup[1]=200
print(tup)
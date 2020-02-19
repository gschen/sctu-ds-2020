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
print("我叫%s"%('lisa'))
print("我今年%d"%(19))


#列表
list=[1,2,3,[4,5,6]]
print(len(list))
for x in range(len(list)):
    print(list[x])
#添加
list.append(7)
list.extend([1,2])
print(list)

#删除
list.pop()

#索引
print(list.index(2))
list=list.sort(list)

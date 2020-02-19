a="he"
b="r"
print(a+b)

c="lee"
print(c*4)

str="apple"
print(str[1])
print(str[-1])
print(str[1:3])

#格式化输出
print('我的名字是%s'%('jf'))
print('我今年%d'%(20))

#列表
list=[1,3,[4,5,6]]
print(len(list))
for x in range(len(list)):
    print(list[x])
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
print(tup)


a="hi"
b="s"
print(a+b)
#2

c="hi"
print(c*3)
str1="abcde"
print(str1[0])
print(str1[-1])
print(str1[0:4])   #左闭右开
#格式化输出
print("我叫%s"%("张三"))
print("我今年%d岁"%(10))
#列表
list=[1,2,3,[4,5,6]]
print(len(list))

#迭代
for x in range(len(list)):
    print(list[x])


#
list=[1,2,3,[4,5,6]]
list.append(7)
list.extend([1,2])
print(list.index(2))

lis1=[5,4,2,8,3,8]
lis1.sort()
print(lis1)
lis1.pop()  #默认最后一个元素

#元组
tup=("s",100,[1,2])
print(tup)
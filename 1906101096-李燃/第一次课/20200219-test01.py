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
print('我叫%s'%('张三'))
print('我今年%d'%(10))

#列表
lis1=[1,2,3,[4,5,6]]
print (len(lis1))
lis1.append(7)
lis1.extend([1,2])
print(lis1.index(2))

#排序
lis2=[5,7,6,8,3,1,2]
lis2.sort()
print(lis2)

#元组
tup=('s',100,[1,2])
tup[1]=200    #元组元素唯一，不能更改
print(tup)

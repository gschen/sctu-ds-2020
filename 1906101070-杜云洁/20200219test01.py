#连接字符
a='hi'
b='s'
print(a+b)
#重复字符
c='hi'
print(c*3)
#切片
str='abcde'
print(str[0])
print(str[0:4])
#判断
a='abcd'
print('e' in a)
print('i' in a)
#格式化输出
print('我叫%s' %('张三'))
print('我今年%d'%(18))
#列表
list=[1,2,3,[4,5,6]]
print(len(list))
for x in [1,2,3]:
    print(x)
list.append(7)
print(list.pop(1))
list.extend([1,2])
print(list)
print(list.index(2))
#排序
list=[5,7,4,3,6,2]
list.sort()
print(list)
#元祖
#元祖中的元素种类不限
tup=('s',100,[1,2])
print(tup)
#tup[100]=200
#print(tup)  报错，元祖中的元素不能更改.
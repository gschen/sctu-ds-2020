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

#成员运算符
a="bcde"
print("e"in a)
print("f"not in a )

#格式输出
print('我叫%s'%('张三'))
print('我今年%d'%(10))

#列表
lis1=[1,2,3,[4,5,6]]
print(len(lis1))

for x in range(len(lis1)):  #迭代
    print(lis1[x])

#排序
list=[5,7,4,3,6,2]
list.sort()
print(list)
#元祖
tup=('s',100,[1,2])
print(tup)
#tup[100]=200
#print(tup)

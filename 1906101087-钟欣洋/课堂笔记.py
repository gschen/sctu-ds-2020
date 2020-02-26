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
print("我叫%s"%('钟欣洋'))
print("我今年%d"%(10))


#列表
lis1=[1,2,3,[4,5,6]]
print(len(lis1))

for x in [1,2,3]:
    print(x)

lis2 = [1,2,3[4,5,6]]
lis2.append(7)
lis2.extend([1,2])
lis2.pop(1)#通过下标删值，默认是最后一个
print(lis2)

lis3=[5,4,3,2,8,3,8]
lis3.sort()
print(lis3)


#元组
tup=('s',100,[1,2])
#tup[1]=200 元组元素不能被修改
print(tup)

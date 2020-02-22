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
print("我叫%s"%('张三'))
print("我今年%s"%(10))




#列表
lis1=[5,4,2,8,3,8]
#lis1.append(7)
#lis1.extend([1,2])
lis1.pop(1)#通过下标删值，默认是最后一个
#lis1=lis1.sort()
print(lis1)

#元组
tup=('s',100,[1,2])
#tup[1]=200    元组元素不能改变
print(tup)
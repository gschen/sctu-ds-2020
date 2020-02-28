#连接字符
a='hi'
b='s'
print(a+b)
#重复字符
c='hi'
print(c*3)

#切片
str1='abcde'
print(str[0])
print(str1[-1])
print(str1[0:4])


#格式化输出
print('我叫%s'%('张三'))
print('我今年%d'%(10))

#列表
list1=[5,4,2,8,3.8]
#list1.append(7)
#list1.extend([1,2])
list1.pop(1)#通过下标删值，默认是最后一个
#list1.sort()
print(list1)

#元组
tup=('s',100[1,2])
#tup[1]=200 元组元素不能被更改
print(tup)
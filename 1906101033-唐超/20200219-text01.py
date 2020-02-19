#连接字符
a='hi'
b='s'
print(a+b)
#重复字符

c='hi'
print(c*3)


str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:5])


a='abcd'
'e' in a

#   格式化输出
print('我叫%s'%('唐超'))
print('我今年%d'%(19))

#列表
#len
list=[1,2,3,[5,6]]
print(len(list))

for x in [1,2,3,[4,5,6]]:
    print(x)

list.append(7) #添加
print(list)
list.extend([1,2,3])#删除
print(list)
print(list.index(3))
print(list.pop(0)) #删除

list1=[2,5,6,9,4]
list1.sort()
print(list1)

#元组
tup=('a',99,[1,2])
print(tup)                  #元组元素不能更改
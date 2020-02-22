#连接字符
a = 'hi'
b = 's'
print(a+b)

#重复字符
c = 'hi'
print(c*3)

#切片
str1 = 'abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])

#判断
print('a' in str1)
print('f' in str1)

#格式化输出
print("我叫%s"%('张三'))
print("我今年%d"%(10))

#列表
list1 = [1,2,3,[4,5,6]]
print(len(list1))

#增加、删除、排序
#list1.append(7)
#list1.extend([1,2])
#list1 = list1.sort()
list1.pop(3)
print(list1)

#迭代
for i in [1,2,3,4]:
    print(i)

#元祖(不可修改)
tup = ('w',100,[1,2])
print(tup)



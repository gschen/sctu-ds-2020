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

a='abcd'
print('a' in a)
print('a' not in a)

#格式化输出
print('我叫%s'%('肖文星'))
print('我今年%d'%(19))

#列表
list1=[1,2,3,[4,5,6]]
print(len(list1))
list1.append(7)
print(list1)
list1.extend([1,2])
print(list1)
print(list1.index(1))

list2=[9,1,6,5,7,3]
list2.sort()
print(list2)

list3=[1,2,3]
list3.pop()
print(list3)
list4=[1,2,3]
list4.pop(1)
print(list4)
#迭代
for i in [1,2,3]:
    print(i)


#元组
tup=('a',100,[1,2])
print(tup)

#tup[1]=200  会报错
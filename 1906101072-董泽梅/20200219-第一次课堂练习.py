a='hi'
b='s'
print(a+b)
#重复字符
c='hi'
print(c*3)
#切片
str='abcde'
print(str[0],str[-1])
print(str[0:4])
#判断
print('e' in a)
print('i' in a)

#格式化输出
print('我叫%s' %('张三'))
print('我今年%d'%(19))

#列表
list=[1,2,3,[4,5,6]]
print(len(list))

#迭代
for x in [1,2,3]:
    print(x)

#增加删除
# list.append(7)
# print(list)
# list.extend([1,2])
# print(list)
# print(list.index(2))
# print(list.pop(1))

#排序
list1=[5,7,4,3,6,2]
print(sorted(list1))

#元祖(元祖中的元素不能更改)
tup=('s',100,[1,2])
tup[1]=200
print(tup)

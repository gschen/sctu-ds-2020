# 字符运算
a='hello'
b='world'
print(a+b)
c='he!'
print(c*3)


# 切片
str='sdafsafa'
print(str[1],str[-1])
print(str[0:5])

# 格式化输出
print('我是%s' % '张三')
print('我今年%d岁' % (10))


# 列表
list=[1,2,3,[4,5,6]]
print(len(list))
# 列表元素的增添与删除
list.append(7)
list.pop(1)
print(list)
# 列表排序
list1=[7,5,2,6,9,10]
list1.sort()
print(list1)



# 元组
tup = ('a',100,[1,2])
# 尝试修改元组的元素会报错
# tup[1]=200
print(tup)
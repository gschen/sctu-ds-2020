#合并
a='hello'
b='world'
print(a+b)
#重复
c='lianglin'
print(c*5)

#切片
d='abcde'
print(d[0],d[-1])
print(d[2:4])
#判断
print('g' in d,'a' in d,'c' not in d,'g' not in d)

#格式化输出
print('谁是%s'%'小明')
print('5+4=%d'%9)

#列表
print(len([1,2]))
print([3,34,5]+[432,5])
print([1,2]*5)
#迭代
for i in range(1,10):
    print(i)


list=[1,2,3]
#添加
list.append(4)
list.extend([5,6])
print(list)
print(list.index(5))
#删除
list.pop()
list.remove(2)
print(list)

#排序
h=[1,6,8,2,4]
h.sort(reverse=True)
print(h)
print(h.index(1))
h.sort()
print(h)
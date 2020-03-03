#连接
a='hello'
b='python'
print(a+b)

#重复
c='hi'
print(c*5)

#索引
d='python'
print(d[0])
print(d[-1])
print(d[2:])
print(d[:2])
print(d[1:3])

#判断
s='python'
'p' in s
'a' in s
'p' not in s
'a' not in s

#列表中可以嵌套，用len求列表长度
list1=[1,2,3,[4,5,6]]
print(len(list1))

#for循环以及end的用法
s=[1,2,3]
for i in s:
    print(i,end=' ')

#列表的添加，删除，插入等(append,insert,extend,pop,count)
list2=[1,2]
list2.append(3)
print(list2)
list2.extend([4,5])
print(list2)
print(list2.count(2))
list2.insert(4,8)
print(list2)
k=[1,2,3]
k.pop() #如果pop中没有给定数值，默认删除最后一个元素
k.pop(1)
print(k)

#升序和降序排列
m=[3,2,5,6,1]
m.sort()
print(m)
m.sort(reverse=True)
print(m)

#元组中的数据类型多样
n=(100,'s')
# n(0)=200 #对于元组中的元素，不可以修改
print(n)
#连接字符
a='hi'
b='s'
print(a+b)
#重复字符
c='hi'
print(c*3)
#格式化输出
print('我叫%S'%("zouting"))
#索引 切片
str1='abccde'
print(str1[0])
print(str1[-1])
print(str1[0:4])
#迭代
for x in [1,2,3]:
    print(x)
   
a='abcd'
'e' in a
'd' in a
'e' not in a
#列表
list=[1,2,3,[4,5,6]]
print(len[list])
#list.append(7)
#list.extend([1,2,3])
list.pop()
list.pop(1)
print(list)

list1=[2,5,6,9,4]
list.sort()
print(list1)

#元组 元组中的元素不能更改
tup=('a',99,[1,2])
tup[1]=200
print(tup)
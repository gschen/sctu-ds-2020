#集合
s={'a','b','c',1}
m=set('aabbcc')
print(s,m)

#差集、并集、交集、补集
print(s-m)
print(s|m)
print(s&m)
print(s^m)

#(add、update)、(discard、remove、pop) pop:随机删除一个元素
s.add('d')
print(s)
s.update({8,9},[3,4],'e') #集合中的元素可以是字典，列表和字符串
print(s)
s.remove(9)
print(s)
s.discard(8)
print(s)
s.pop()
print(s)

#字典:键唯一，值多样
dict1={'name':'张三','age':19,'school':'sctu'}
dict1['name']='李四'
print(dict1)
#get返回指定键的值
dict1.get('name')
dict1.setdefault('age')
dict1.setdefault('address','成都')
print(dict1)
dict1['class']=3
print(dict1)
#删除 del(删除的直接是键对值)、pop(删除的时候必须要写键)、popitem(删除的时候是随机的)
del dict1['name']
print(dict1)
dict1.pop('age')
print(dict1)
dict1.popitem()
print(dict1)
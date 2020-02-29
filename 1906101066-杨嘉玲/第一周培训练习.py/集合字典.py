A = {'a','b',1}
B = set('acg')
#集合的差（补）
print(A-B)
#不同时包含
print(A^B)
#并集
print(A/B)
#交集
print(A&B)

#集合的增
A.add('d')
print(A)
B.update({2,3},[5],'e')
#集合的删除
print(B)
x = A.pop()
print(x)
A.discard('a')
print(A)
B.remove('g')
print(B)

#字典
dict = {'name':'张三','age':10,'school':'sctu'}
#修改
dict['name'] = '李四'
print(dict)
#增加
dict['class'] = '2班'
print(dict)
#查找
x = dict.get('school')
print(x)
dict.setdefault('name')
dict.setdefault('address','成都')
print(dict)
#删除
del dict['age']
print(dict)
dict.pop('class')
print(dict)
dict.popitem()
print(dict)
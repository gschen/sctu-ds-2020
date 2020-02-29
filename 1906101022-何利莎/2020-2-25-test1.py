#集合的两种表示方法
A={'a','b','c','c',1}
B=set('aabbcce')
print(A,B)

#集合的差（补）
print(A-B)
#集合并操作
print(A|B)
#集合的交
print(A&B)
#不同时包含
print(A^B)

#集合的增删
#添加元素的两种方法
A.add('d')
B.update([1,3],[2,4],'e')
print(A)
print(B)

#元素删除的三种方法
A.remove('a')
A.remove('f')
A.discard('f')

A.pop()
print(A)

#字典
dic={'name':'张三','age':19,'school':'sctu'}
print(dic)
#修改数据
dic['name']='李四'
#print(dic)
#查找数据
dic.get('name')
dic.setdefault('name')
dic.setdefault('address','成都')
print(dic)

#增加数据
dic['class']='一班'
print(dic)

#删除数据
del dic['name']
dic.pop('name')
dic.popitem()
print(dic)


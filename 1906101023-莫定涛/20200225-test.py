#构建集合的两种方法

A={'a','b','c','d','c',1}
B=set('aabbcce')
print(A,B)

#集合的并
print(A|B)
#集合的交
print(A&B)
#集合的补
print(A-B)
#集合的不同时包含
print(A^B)
#集合的增删
A.add('e')
B.update({1,3},[4,2],'y')
#删除元素的三种方法
A.remove('a')
A.remove('o')
A.discard('o')
A.pop()

#字典
dic{'name':'李四','age':19,school:'dx'}
print(dic)
#修改数据
dic['name':'张三']
#查找数据
dic.get('name')
dic.get('address')
dic.setdefault('name')
dic.setdefault('address','成都')
#增加数据
dic['class']='1班'
print(dic)
#删除数据
del dic.['name']
print(dic)
dic.pop('name')
print(dic)
dic.popitem()
print(dic)





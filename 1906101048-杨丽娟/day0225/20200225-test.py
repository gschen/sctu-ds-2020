A={'a','b','c','c',1}
B=set('aabbcce')
print(A,B)
#集合的并
print(A|B)
#集合的交
print(A&B)
#不同时的包含
print(A^B)
#集合的补
print(A-B)
#集合的增删
A.add('d')
B.update({1,3},[4,2],'e')
print(A)
print(B)
#删除元素
A.remove('a')
A.discard('f')
A.pop()




#字典
dic={'name':'张三','age':19,'school':'sctu'}
print(dic)
#修改数据
dic['name']='李四'
print(dic)
#查找数据
dic.get('address')
dic.setdefault('name')
print(dic)
#增加数据
dic['class']='一班'
#删除数据
del dic['name']
print(dic)
dic.pop('age')
print(dic)
dic.popitem()
print(dic)










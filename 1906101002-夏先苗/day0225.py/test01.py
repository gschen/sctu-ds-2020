#集合
A={'a','b','c','c',1}
B=set('aabbcce')
print(A,B)
print(A-B)
print(A&B)
print(A|B)
print(A^B)
#添加元素
A.add('a')
print(A)
B.update({1,3},[4,2],'e')
print(B)
#删除元素
A.remove('a')
#A.remove('f')
print(A)
A.discard('f')
print(A)
x=A.pop('b')
print(x)

#字典
dic={'name':'张三','age':18,'school':'sctu'}
print(dic)
#修改数据
dic['name']='李四'
#查找数据
dic.get('name')
dic.setdefault('address','成都')
print(dic)
#增加数据
dic['class']='1班'
print(dic)
#删除数据
del dic['name']
dic.pop('age')
print(dic)
dic.popitem()
print(dic)

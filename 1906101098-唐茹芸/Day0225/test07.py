A={'a','b','c','c',1}
B=set('aabbcce')
print(A,B)
print(A-B)
print(A|B)
print(A&B)
print(A^B)



A.add('a')
B.update({1,3},[4,2],'e')
print('A')
print('B')



A.remove('a')
A.remove('f')
A.discard('f')


A.pop()
print(A)

#字典
dic={'name':'张三','age':19,'school':'sctu'}
print(dic)
dic['name']='李四'
dic.get'address')
dic.setdefault('name')
print(dict)
dic['class']='1班'
print(dic)


del dic['name']
print(dic)
dic.pop('age')
print(dic)

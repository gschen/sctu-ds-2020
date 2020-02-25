# 集合
A = {'a','b','c',1}
B=set('aabbccce')
print(A,B)

#并集 
print(A|B)


#交集
print(A&B)

#补集
print(A-B)
print(B-A)
#不同时包含
print(A^B)

#集合的增删
A.add('d')
print(A)

B.update({1,3},[4,2],'e')
print(B)

# 删除的三种方法

A.remove('a')
#A.remove('f')
A.discard('f')

A.pop()
print(A)

#字典
dic={'name':'张三','age':19,'school':'sctu'}
# 查找
dic['name']='李四'
print(dic)
print(dic.get('name'))
print(dic.setdefault('address','成都'))
#dic.get('address')
#print(dic)
# 增加数据
dic['class']='1班'
print(dic)
#删除
del dic['name']
print(dic)
dic.pop('age')
print(dic)
dic.popitem()
print(dic)
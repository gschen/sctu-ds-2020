A={'a','b','c','c'}
B=set('aabbccef')
#集合的并
print(A|B)
#集合的交
print(A&B)
#集合的差
print(B-A)
#不同时包含
print(A^B)
#两种方式添加
A.add('e')
B.update({1,3},[2,4],'e')
print(A)
print(B)
#三种方式删除
A.remove('a')
A.discard('b')
A.pop()
print(A)



#字典
dic={'name':'张三','age':'18','school':'sctu'}
print(dic)
#修改数据
dic['name']='李四'
print(dic)
#查找数据
dic.get('name')
dic.setdefault('address',default='成都')
print(dic)

#增加数据
dic['class']='2班'
print(dic)


#删除数据
del dic['age']
dic.pop('name')
dic.popitem()
print(dic)
#集合
A={'a','b','d',1}
B=set('aabbcce')
#集合的交
print(A&B)
#集合的并
print(A|B)
#集合的差
print(B-A)
#不同时包含
print(A^B)
#增加元素
A.add('h')
print(A)
B.update({1,3},[2,4],"t")
print(B)
#删除元素
A.remove('a')
print(A)
B.discard('c')
print(B)
#POP随机删除元素
B.pop()
print(B)


#字典
#修改数据
dic={'name':'张三','age':19,'school':'sctu'}
dic['name']='李四'
print(dic)
#查找数据
dic.get('name')
print(dic)
dic.setdefault('name')
print(dic)
#增加数据
dic['class']='1'
print(dic)
dic.setdefault('address','成都')
print(dic)
#删除数据
del dic['name']#必须给定值
print(dic)
dic.pop('age')#必须给定值
print(dic)
#随机返回并删除字典中最后的值
dic.popitem()
print(dic)


#条件循环和判断







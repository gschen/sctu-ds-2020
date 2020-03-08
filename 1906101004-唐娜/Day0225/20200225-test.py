#集合
A={'a','b','c','c',1}
B=set('aabbcce')
print(A,B)

#集合的运算
#集合的差（补）
print(B-A)    #返回{'e'}
#集合的并
print(A|B)
#集合的交
print(A&B)
#集合的不同时包含
print(A^B)   #返回{'e',1}

#集合的增删
#添加元素的两种方法
A.add('a')
print(A)

B.update({1,3},[4,2],'e')
print(B)


#删除元素的三种方法
A.remove('a')
A.remove('f')#元素不存在，会报错
A.discard('b')
A.discard('f')#元素不存在，不会报错
print(A)

A.pop()#随机删除元素
print(A)

#字典，键必须唯一，值可以多样
dic={'name':'张三','age':19,'school':'sctu'}
#修改数据
dic['name']='李四'
print(dic)
#查找数据
dic.get('name')
dic.get('address')
dic.setdefault('address',default='成都')
#增加数据
dic['class']='1班'
print(dic)

#删除数据
del dic['name']
dic.pop('age') #返回被删除的
dic.popitem() #随机返回并删除最后一对键和值
print(dic)
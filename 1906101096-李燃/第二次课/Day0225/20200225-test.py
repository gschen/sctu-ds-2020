#集合
#构建集合的两种方法

A={'a','b','c','c',1}#每个元素用逗号隔开，字符串要加定界符

B=set('aabbcce')#用小括号

print(A,B)

print(A|B)#集合的并

print(A&B)#集合的交集

print(A^B)#不同时的包含

print(B-A)#集合的差（补）集

#集合的增删
#添加元素--2种
A.add('d')      #add():当元素存在时不操作
B.update({1,3},[4,2],'e')#update():添加元素，可以是列表，字典
print(A)
print(B)

#删除元素--3种
A.remove('a')
A.remove('f')   #remove():删除元素时，元素不存在时会报错
A.discard('f')    #discard():元素不存在时不会报错


A.pop()
print(A)    #pop():随即删除，并且返回的是被删除的元素






#字典


dic={'name':'张三','age':19,'school':'sctu'}
print(dic)

#修改数据
dic['name']='李四'
print(dic)

#查找数据
dic.get('name')
dic.setdefault('name')
print(dic)

#增加数据
dic['class']='3班'
print(dic)

#删除数据--3种
del dic['name']# 括号里是键，删除时键和对应的值同时删除
dic.pop('age')
dic.popitem()# 随机返回删除的值
print(dic)

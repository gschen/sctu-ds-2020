#集合
#构建集合的两种方法

A={'a','b','c','c'}#每个元素用逗号隔开，字符串类型的数据需要加界定符
B=set('aabbbcc')#注意使用的是小括号，所有元素放在一起
print(B)

#集合之间的运算
#集合的差（补）
print(A-B)
#集合的并操作
print(A|B)
#集合的交
print(A&B)
#不同时包含
print(A^B)

#集合的增删
#添加元素的两种方法
A.add('a')#元素存在时不操作
print(A)
B.update({1,3},[2,4],'e')#包含多种参数类型
print(B)

#删除元素的三种方法
A.remove('a')#元素不存在会报错
print(A)
A.remove('f')
print(A)
A.discard('f')#元素不存在不会报错
print(A)
A.pop()#随机删除元素，并返回被删除元素
print(A)


#字典（键必须唯一，值可多样）
dic={'name':'张三','age':19,'school':'sctu'}
#print(dic)

#修改数据
dic['name']='李四'
print(dic)
#查找数据
dic.get('address')#若值不存在返回default,默认为空值
dic.setdefault('name')
dic.setdefault('address','成都')
print(dic)
#增加数据
dic['class']='1班'
print(dic)

#删除数据
del dic['name']#同时删除键和对应的值
print(dic)

dic.pop('age')#键值必须给出
print(dic)
dic.popitem()#不需要给键的参数，删除最后一个
print(dic)
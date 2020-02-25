#集合
#构建集合的两种方法
A={'a','b','c','c',1}#每个元素用逗号隔开，字符串类型的数据需要加定界符
B=set('aabbcce')#注意使用的是小括号，所有元素放在一起
#print(A,B)
#集合之间的运算
#集合的差（补）
#print(B-A)
#集合的并操作
#print(A|B)
#集合的交
#print(A&B)
#不同时包含
print(A^B)


#A.add('d')
#print(A)
# B.update({1,3},[4,2],'e')
# print(B)

#A.remove('a')
#A.remove('f')
#A.discard('f')
#A.pop()
#print(A)

#字典
#dic={'name':'张三','age':19,'school':'sctu'}
#修改数据
#dic['name']='李四'
#查找数据
#dic.get('address')
#dic.setdefault('name')
#print(dic)
#增加数据
#dic['class']='1班'
#print(dic)
#删除数据
#del dic['name']
#dic.pop('age')
#print(dic)
#dic.popitem()



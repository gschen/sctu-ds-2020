A = {'a','b','c','c',1}#然后每个元素用逗号隔开，字符串类型的输出需要加定界符
B=set('aabbcc')#注意使用的是小括号，所有元素放在一起
#print(A,B)


#集合间的运算
#集合的(补)
#print(B-A)
#集合的并操作
#print(A|B)
#集合的交
#print(A&B)
#不同时包含
#print(A^B)

#集合的增删
#增加元素的两种方法
#A.add('d')
#B.update({1,3},[2,4],"e")
#print(A)
#print(B)

#删除集合中的元素
#A.remove('a')
#B.discard('f')

# A.pop()
# print(A)

#字典

dic={'name':'张三','age':13,'school':'sctu'}
#print(dic)

#修改数据
dic['name']:'李四'
#查找数据
# dic.get('address')
# dic.serdefault('name')
# dic.serdefault('address','成都')
# print(dic)
# 增加数据
#dic['class']='1班'

# 删除数据
#del dic['name']

#dic.pop('age')
#print(dic)
#dic.popitem()
#print(dic)
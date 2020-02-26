# coding=utf-8

'''集合'''

# 构建集合的两种方法

A={'a','b','c','c',1} # 每个元素用逗号隔开，字符串类型需加定界符
B=set('aabbcce') # 注意小括号，所有元素放在一起
print(A,B)

# 集合的基本操作：并，交，补
# 集合的差(补)
print(A-B)
print(B-A)
# 集合的并操作
print(A|B)
# 集合的交
print(A&B)
# 不同时包含
print(A^B)

# 集合的增删
# 添加元素的两种方法
# A.add('d') # 当元素存在时则不操作
# B.update({1,3},[4,2],'e') # 增加元素可以是字典，列表
# print(A)
# print(B)

# 删除元素的三种方法
# A.remove('a')
# A.remove('f') # remove 元素不存在会报错
# A.discard('f') # 删除元素不存在也不会报错
# A.pop() # 随机删除元素，并返回被删除的元素


'''字典'''
# 特点：键必须唯一，值可以多样
dic={'name':'张三','age':19,'school':'sctu'}
print(dic)

# 修改数据
dic['name']='李四'
print(dic)

# 查找数据
print(dic.get('name')) # 如果元素不存在，不返回值
print(dic.setdefault('name'))
print(dic.setdefault('address','成都')) # 不存在的元素，setdefault会直接添加元素

# 增加数据
dic['class']='1班'
print(dic)

# 删除数据
del dic['age']
print(dic)

dic.pop('name')
print(dic)

dic.popitem() # 随机删除键和值
print(dic)

# dic.clear() # 删除所有元素
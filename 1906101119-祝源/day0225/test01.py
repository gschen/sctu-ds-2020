# 集合
# 构建集合的两种方法

A = {'a','b','c','c',1}# 然和每个元素用逗号隔开，字符串类型的数据需要加定界符

B = set('aabbcce')# 注意使用的是小括号，所有元素放在一起
print(A,B)

#集合之间的的运算
# 集合的差补
# print(A-B)
# 集合的并操作
# print(A|B)
# 集合的交
# print(A&B)
# 不同时包含
# print(A^B)

# 集合的增删
# 添加元素的两种方法
A.add('a')
# B.update({1,3},{4,2},'e')
print(A)
# print(B)

# 删除元素的两种方法

# A.remove('a')
# A.remove('f')
A.discard('f')

 x=A.pop()
 print(x)

# 字典

dic = {'name':'张三','age':19,'school':'sctu'}

# 修改数据
dic['name'] = '李四'

# 查找数据
# dic.get('address')
# dic.setdefault('name')
# dic.setdefault('address', default = '成都')
# print(dic)

# 增加数据
dic['class'] = '3班'

#删除数据
del dic['name']
print(dic)
# dic.pop('name')
# dic.popitem()
# print(dic)

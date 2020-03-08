A={'a','b','c','c',1}
B=set('aabbcce')
#集合的并
#print(A|B)
#集合的交
#print(A&B)
#集合的差（补）
#print(B-A)
#集合的不同时包含
#print(A^B)

#集合的增减
#添加元素的两种方式
#A.add('a') 当元素存在时则不操作
#B.update({1,3},{4,2},'e') 添加的元素可以是列表 元组 字典等
#删除集合中的元素
#A.remove('a') A.rmove('f')  移除指定元素如果要删除的元素不存在则会报错
#A.dicard('f') 与remove相反 元素不存在不会报错
#a.pop() 随机移除元素
#print(A)

#字典
#dic={'name':'张三'，'age':19,'school':'abc'}
#1 修改数据 
# dic['name']='李四'
# print(dic)
# 查找数据
# dic.get('address')
# dic.setdefault('name')
# dic.setdefault('address','成都'）
# print(dic)
# 增加数据
# dic['class']='3班'
# 删除数据
# del dic['name']
# print
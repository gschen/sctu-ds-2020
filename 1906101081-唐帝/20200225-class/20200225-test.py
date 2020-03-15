# 集合
# 构建集合的两种方法
A={'a','b','c','c',1}
B=set('aabbcc')
# 集合的差（补）
print(A-B)
print(B-A)
# 集合的并操作
print(A)
# 集合的交
print(A&B)
# 不同时包含
print(A^B)
# 集合的增删
# 添加元素的两种方法
A.add('a')
B.update({1,3},{4,2},'e')
print(A)
print(B)
#删除元素的三种方法
#  若元素不存在，remove将报错
#  A.remove('f')
A.remove('a')
# 若元素不存在，discard不会报错
A.discard('f')
# pop 随机删除元素
A.pop()


# 字典
# 键必须唯一，值可以多样
dic={'name':'张三','age':19,'school':'sctu'}
# 修改数据
dic['name']='李四'
print(dic)
# 查找数据，若没有该数据，则不会返回值
dic.get('adress')
dic.setdefault('address','成都')
print(dic)
# 增加数据
dic['class']='一班'
# 删除数据
dic.pop('age')
print(dic)
dic.popitem()
print(dic)


#
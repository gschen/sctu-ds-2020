#集合
#构建集合的两种方法
A={'a','b','c','1'}
B=set('aabbcc')
print(A,B)
#集合的基本操作
#差(补)：print(A-B)
#并：print(A|B)
#交：print(A&B)
#不同时包含：print(A^B)
#集合的增加删除
#添加元素的两种方法
# A.add('d')
# B.update({1,3},[4,2],'e')
# print(A)
# print(B)
#删除元素的三种方法
# A.remove('f')
# A.discard('f')
# A.pop()
# print(A)


#字典(键必须唯一，值可以多样)
dic={'name':'张三','age':19,'school':'sctu'}
print(dic)
#修改数据
dic['name']='李四'
print(dic)
# #查找数据
dic.get('name')
dic.setdefault('address','成都')
print(dic)
#增加数据
dic['class']='2班'
#删除数据
#del dic['name'] 
dic.pop('name')
dic.popitem()
print(dic)



#集合
#构建集合两种方法
A={'a','b','c',1}
B=set('aabbcc')
#print(A,B)
#元素没有顺序的
#集合的基本操作（并，交，补）
#补
#print(A-B)
#并
#print(A|B)
#交
#print(A&B)
#不同时包含
print(A^B)


#集合的增添
#增添元素的两种方法
#A.add('a')
#B.update({1,3},[4,2],'e')
#print(A)
#print(B)


#删除元素的二种方法
#A.remove('a')
#A.discard('f')
#A.remove('f')
#A.pop()


#字典
#字典格式: d={key1:value1,key2:value2}
dic = {'name':'张三','age':'18','school':'sctu'}
print(dic)
#修改数据
dic['name']='李四'
print(dic)
#查找数据
dic.get('name')
dic.setdefault('name')
print(dic)
#增加数据
dic['class']='1班'
print(dic)

#删除数据
#del dic['name']
#print(dic)
#dic.pop('age')
#dic.popitem()
#print(dic)




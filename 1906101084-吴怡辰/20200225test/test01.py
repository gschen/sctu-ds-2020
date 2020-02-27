A = {'a','b','c','c',1}

B = set('aabbcce')
print(A,B)

# 集合运算
print(A|B) #交
print(A&B) #并
print(A-B) #补()
print(A^B) #不同时包含

# 集合增删
A.add('d') #不重复增加
B.update({1,2},[3,4],'e') 
A.remove('a')
#A.remove('f')
A.discard('f')
A.pop() #随机删除元素
#A.clear() #删除所有元素
print(A)
print(B)


# dict
dict = {'name':'张三','age':'18','school':'sctu'}
dict['name'] = '李四' #修改数据
dict['class'] = '3班' #增加
dict.get('name') #获取
dict.setdefault('address','成都')
del dict['name']
dict.pop('age') 
dict.popitem() #删除最后一对键值对
print(dict)


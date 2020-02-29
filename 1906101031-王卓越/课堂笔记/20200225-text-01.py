#集合
A={'a','b','c','c',1}#集合具有元素的唯一性
# B=set('aabbcc')#set返回的是一个集合
# print(A,B)

 #补集
# print(A-B)

 #并集
# print(A|B)

 #交集
# print(A&B)

 #不同时的包含
# print(A^B)

 #增加元素
# A.add('k')
# A.update({1,3},[4,2],'e')
# print(A)

#删除元素
# A.pop()#集合中的pop随机删除元素
# # A.remove('b')
# # A.discard('k')#即使元素不存在于集合，也不会报错
# print(A)

#字典
dic={'name':'张三','age':'19','sex':'男'}
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# for x in dic:
#     print('{}:{}'.format(x,dic[x]),end='')
# print('')
print(dic.get('id'))
dic['id']=5
print(dic)
#删除数据
del dic['id']
dic.pop('name')
dic.popitem()#随即返回并删除一对键值对
print(dic)
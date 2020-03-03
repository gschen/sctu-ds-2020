#集合
#构建集合的两种方法
A={'a','b','c','c',1} #每个元素用逗号隔开，字符串类型的数据需要加引号
B=set('aabbcce') #set是使用()将元素括起来，且元素与元素之间无间隔
# print(A,B)
#集合之间的运算
# print(A|B) #并集运算
# print(A&B) #交集运算
# print(A-B) #补集运算
# print(B-A)
# print(A^B) #不同时包含

#集合的增删
#增加元素的两种方法
A.add('d')
print(A)
B.update({1,3},[4,2],'e')
print(B)
#删除元素的三种方法
# A.remove('a')
# A.remove('f')
# A.discard('f') #删除不在集合里面的字母，不报错
x=A.pop() #随机删除一个数
# print(A)
# print(B)

#字典
dic={'name':'张三','age':18,'school':'sctu'}
# print(dic)
#修改数据
# dic['name']='李四'
# print(dic)
#查找数据
# dic.get('name')
# print(dic.get)
# dic.get('address')
# dic.setdefault('name')
# dic.setdefault('address',default='成都')
# print(dic.setdefault)
#增加数据
# dic['class']='1班'
# print(dic)
#删除数据
# del dic['name']
# dic.pop('age')
dic.popitem() #popitem()是删除最后一个key
print(dic)
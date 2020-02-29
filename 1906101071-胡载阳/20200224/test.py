A={'a','b','c','c','1'}
B=set('aabbcce')
#print(A,B)

print(B-A)
print(A|B)
print(A&B)
print(A^B)
















#A.add('a')
#B.update({1,3},[4,2],'e')
#print(A)
#print(B)



#A.remove('a')
A.remove('f')
#A.discard('f')

#x=A.pop()
#print(x)


#字典

dic={'name':'张三','age':19,'school':'sctu'}

#修改数据
dic['name']='李四'
print(dic)
#查找数据
#dic.get('address')
#dic.setdefault('name')
#dic.setdefault('address','成都')
print(dic)

#增加数据
dic['class']='1班'
print(dic)

#删除数据
del dic['name']
print(dic)
dic.pop('age')
dic.pop('neme')
dic.popitem()
print(dic)






















a={'a','c','v','v',1}
b=(set('zwsa'))

print(a|b)  #并集
print(a-b)  #补集
print(a&b)   #交集
print(a^b)   #不同时包含
a.add('q')  #添加元素，但加入相同不重复
print(a)
b.update({1,2},[4,3],'l')  #元素添加可以是列表，元组，str
print(b)  
a.remove('c')  #删除元素，如果列表无此元素就报错
print(a)
a.discard('d')   #删除元素，无此元素也不会报错
print(a)
a.pop() #s随机删除
print(a)


字典
dic={'name':'zhanshan','age':19,'school':'qhinghua'}
print(dic)
xiu gaishuju
dic['name']='lisi'
print(dic)

#查找数据

dic.get('name')
print(dic)
dic.setdefault('name')
print(dic)

#tianj添加数据
#dic['class']='class one'
#print(dic)


#删除数据
#del dic['name']
#print(dic)

#dic.pop('name')
#print(dic)


#dic.popitem()
#print(dic)
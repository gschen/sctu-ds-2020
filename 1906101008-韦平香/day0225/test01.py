#集合的基本操作：并交补
A={'a','b','c','c',1}
B=set('aabbcce')
#集合的并
#print(A|B)
#集合的交
#print(A&B)
#集合的差（补）
#print(B-A)
#不同时包含
#print(A^B)
#添加元素
#x=A.add('a')#元素存在时不操作
#x=B.update([1,3],[4,2],'e')#包含多种参数类型
#x=A.remove('a')
#x=A.discard('c')
#x=A.pop('a')
#print(x)

#删除元素的三种方法
#A.remove('a')#元素不存在会报错
A.remove('f')
A.discard('f')#元素不存在不会报错
A.pop()#随机删除元素，并返回被删除元素


#字典(键必须唯一，值可多样）
dic={'name':'张三'，'age':'20','school':'sctu'}
print(dict)
#修改数据
dic['name']='陆驿'
print(dict)
#查找数据
dic.get('address')#若值不存在返回default，默认为空值
dic.setdefault('name')
dic.setdefault('address',default='成都')
print(dict)
#增加元素
dic['class']='1'
print(dic)

#删除元素
del dic['name']同时删除键和对应的值，
dic.pop('name')#键值必须给出
print(dic)
dic.popitem()不需要给键的参数，删除最后一个
print(dic)
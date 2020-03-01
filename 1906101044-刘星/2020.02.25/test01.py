#集合
#构建
A={'a','b','c','c',1}
B=set('aabbcce')
#集合并
print(A|B)
#集合交
print(A&B)
#集合差
print(B-A)
#不同时包含
print(A^B)
#元素的添加
A.add('d')
A.add('a')
print(A)
B.update([1,3],{2,4},'r')
print(B)
#元素的删除
A.remove('a')
#A.remove('f')#用remove删除不存在的元素会报错
A.discard('f')#用discard删除不存在的元素不会报错
A.pop()#随机删除其中一个
print(A)

#字典
dic={'name':'刘星','age':20,'school':'sctu'}
#修改
dic['name']='liuxing'
print(dic)
#查找
dic.get('address')
print(dic)
#增加
dic['class']='2班'
print(dic)
#删除
del dic['name']
dic.pop('age')
dic.popitem()#默认最后一个删除最后一个
print(dic)




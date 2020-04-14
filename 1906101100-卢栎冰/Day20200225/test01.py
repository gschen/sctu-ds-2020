A={'a','b','c','c',1}
B=set('aabbcce')
#集合的交并补#
print(A,B)
print(A-B)
print(A&B)
print(A^B)
print(B-A)

#元素的增减#
B.update([1,3],{4,2},'e')
A.add('a')
print(A)
print(B)
#remove元素不存在会报错#
#discard元素不存在不报错#
A.remove('a')
A.discard('f')
print(A)
#pop随机删除元素#
A.pop()
print(A)

#字典dic{key:value}
dic={'name':'张三','age':19,'school':'sctu'}
print(dic)
#修改数据
dic['name']='李四'
print(dic)
#查找数据
dic.get('address',default='成都')

#增加数据
dic['class']='3班'
print(dic)

#删除数据
del dic['name']
dic.pop







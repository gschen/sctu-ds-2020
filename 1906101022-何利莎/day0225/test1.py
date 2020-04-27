#集合
A={"a","b","c"}
B=set("aabbcce")
print(A-B)#集合相减
print(A&B)
print(A^B)#不同时包含
print(A|B)#并集

#集合的增添
A.add("n")
B.update({1,3},[2,4],{"e"})

#删除元素
A.remove("a")#不存在，会报错
A.discard("f")#不会报错
A.pop()#随机删除

#字典
dic={'name':'lz','age':19,'school':'sctu'}

#修改数据
dic['name']='李'
print(dic)

#查找数据
dic.get('name')
dic.setdefault('name')

#增加数据
dic['class']='1班'
print(dic)

#删除数据
del dic['name']
dic.pop('name')
dic.popitem('class')
print(dic)
#集合
# 构建集合的两种方法 
A={'a','b','c','c'}
B=set('aabbcce')#小括号，所有集合放在一起
print(A,B)

#集合之间的运算
print(A-B)#集合的差（补）
print(A/B)#集合的并      
print(A&B)#集合的交
print(A^B)#不同时包含          

#集合的增删
#添加元素的三种方法       
A.add('d')
B.update({1,3},{4,2}'e')

#删除元素的三种方法
A.remove('a')#元素不存在会报错
A.remove('f')
A.discard('f')#元素不存在不会报错
A.pop()#随机删除元素，并返回被删除元素


#字典(键必须唯一，值可多样)
dic={'name':'张三'，'age':'19','school':'sctu'}
print(dic)

#修改数据
dic['name']='李四'
print(dic)
#查找数据
dic.get('address')#若值不存在返回default,默认为空值
dic.setdefault('name')
dic.setdefault('address','成都')
print(dic)
#增加数据
dic=['class']='1班'
print(dic)
#删除数据
def dic['name']
dic.pop('name')
dic.popitem()
print(dic) 
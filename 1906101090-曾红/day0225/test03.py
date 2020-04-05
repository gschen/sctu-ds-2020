# 集合
# A={'a','b','c','c',1}
# B=set('aabbcce')
# print(A,B)
# print(A-B)              # 集合a中包含而集合b中不包含的元素
# print(A&B)              # 交集
# print(A|B)              # 并集
# print(A^B)              # 不同时包含于a和b的元素


# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print('orange' in basket  )  #判断元素是否在集合中

#添加元素
# A.add('a')                #如果元素已存在，则不进行任何操作
# print(A)
# B.update({1,3},[4,6],'e')
# print(B)

#删除元素
# A.remove('a')
# A.remove('f')                      # 不存在会发生错误
# print(A)
# A.discard('f')
# print(A)                         # 不存在不会发生错误
# x=A.pop()                          #返回最后的值
# print(x)


#字典
# dic={'name':'张三','age':'18','school':'sctu'}
#print(dic)
#修改数据
# dic['name']='李四'
# print(dic)
#查找数据
# dic.get('name')
# dic.setdefault('address','成都')
# print(dic)
#增加数据
# dic['class']='3班'
# print(dic)
#删除数据
# del dic['name']                   # 删除键 'Name'
# dic.pop('age')
# del dict                          # 删除字典
# print(dic)
# dic.popitem()                     #随机返回并删除字典中的最后一对键和值
# print(dic)
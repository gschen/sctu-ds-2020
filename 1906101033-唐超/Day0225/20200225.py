




#集合
#构建集合两种方法
A={'a','b','c','c' ,1}#然后每个元素用逗号隔开，字符串类型的数据需要加定界符。
B=set( ' aabbcce' )#注意使用的是小括号，所有元素放在一起。
#print(A,B) 
#集合之间的运算
#集合的差(补)
print(A-B)
#集合的并操作
#print(A|B) 
#集合的交
#print(A&B )
#不同时包含
#print(A^B)


#集合的增删
#添加元素的两种方法
A. add('A'D I
#B.update({1,3},[4,2],'e')
print(A)
#print(B)


#删除元素的三种方法
#A. remove('a')
#A. remove('f' )
#A.discard('f')
# A.pop()
# print(A)



#字典（特点：键必须唯一，值可以多样） 
#格式：dic={'name': '张三'，" age' :19,'school': 'sctu'}


#修改数据
#格式：dic['name']='李四'
#      print(dic)





#查找数据
#dic.get('name') get 返回指定键的值
# dic.setdefault('address' , default='成都' )
# print(dic)

#增加数据
dic['class']= '1班'
print(dic)

#删除数据
del dic['name']
print(dic)
dic.pop('name')
#dic.popitem()  popitem随机返回并删除字典中的最后一对键和值
print(dic)













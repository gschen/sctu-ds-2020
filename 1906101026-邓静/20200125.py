#集合
#构建集合的两种方法
#A={'a','b','c',1}#然后每个元素用逗号隔开字符类型的数据需要加界符
#B=set('aabbcc')#注意使用的是小括号，所有元素放在一栏
#print(A,B)

#集合之间的运算
#1.集合的差
#print(A-B)
#2.集合的并操作
#print(A|B)
#3.集合的交操作
#print(A&B)
#不同时包含
#print(A^B)

#集合的增加
#添加元素的两种方法
#A.add('a')
#B.update({1,3},[4,2],'e')
#print(A)
#print(B)

#删除元素的三种方法
#A.remove('a')
#A.discard('f')
#A.pop()


#字典
dic={'name':'张三','age':19,'school':'sctu'}
#数据修改
dic['name']='李四'
#查找数据
dic.get('name')
dic.setdefault('address','成都')


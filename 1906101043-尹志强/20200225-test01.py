#集合
#构建集合两种方法(无序的)
A={'a','b','c','c',1}
B=set('aabbcc')
print(A,B)

#集合之间的运算（交，并，补）
#集合的差（补）
#print（A-B）（把前面的作为他的全集）
#集合的并
#print(A|B)
#集合的交
#print(A&B)
#不同时的包含【A中有B中没有】
#print(A^B)

#集合的增加删除
#增添的两种方法
A.add('d')
B.update({1,3},[4,2],'e')#(对于集合字典字符串都可以)
print(B)
#删除的三种方法
A.remove('a')#如果没有元素会报错
A.discard('f')#删除没有的不会报错
A.pop()#随机删除一个数



#字典
#特点：键必须唯一，值可以多样
dic={'name':'张三'，'age':18,'school':'成都。。'}
print(dic)
#修改数据
dic['name']='李四'
#查找数据
#dic.get('name')
#dic.setdefault('address','成都')#（如果不存在这个键，就新加一个，存在就不返回）
#print(dic)
#增加数据
dic['class']='1班'
#删除数据
#del dic['name']#(同时删除对应的值)
#dic,pop('age')#(同时返回并删除对应的值)
#dic.popitem()#（返回并删除最后的键和值）
#print(dic)

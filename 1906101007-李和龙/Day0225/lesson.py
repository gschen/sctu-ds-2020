#构建

A = {"a","f","s","s","w"}
B = set("asdccs")
print(A,B)

#差(补)
print(A-B)

#并
print(A|B)

#交
print(A&B)

#不同时包含
print(A^B)

#增添
A.add("s")
print(A)


A.add("u")
print(A)

B.update({"p","o"},["r","y"],"t")
print(B)

#删除

A.remove("a")
print(A)
A.clear()
print(A)


print(B.pop())
print(B)






#字典
dic=({'name':'张三','age':19,'school':'sctu'})



#修改数据
dic['name']='李四'

print(dic)
#查找数据

dic.get('name')
dic.setdefault('address',default='成都')
print(dic)




# 增加数据
dic['class']='1班'




print(dic)



#删除数据
del dic['name']
dic.pop('age')
print(dic)



dic.popitem()
print(dic)


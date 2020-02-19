a='hi'
b='s'
print(a+b)
#重复字符
c='ho'
print(c*3)

#切片
str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])

#格式化输出
print("我叫%s"%("张三"))
print("我今年%d"%("18"))

#列表
list=[1,2,3,[4,5,6]]
#print(len(list))
#list.append(7)#添加
list.extend([1,2])
list.pop()#删除
list.sort()#排序
print(list)



#元组
tup=('s',100,[1,2])
tup[1]=200
print(tup)
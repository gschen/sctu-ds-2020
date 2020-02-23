 #连接字符
a="h1"
b="s"
print(a+b)
#重复字符

c="hi"
print(c*3)


#切片
str1="abcde"
print(str1[0])#切取第一位
print(str1[-1])#切取最后一位
print(str1[0:4])#切取从第一位a到第四位d

#格式化输出
print("我叫%s"%("张三"))
print("我今年%s"%(10))
# 整数的输出：%0--八位制    %d--十位制  
# 浮点数的输出：%f--默认保留小数点后6位有效数字   


#列表
lis1=[1,2,3,4,5,6,]
#list.append(7)--在添加列表lis1中添加数字7
#list.extend([1,2])#扩展列表，添加元组元素到列表末尾
list.pop(1)#删除第一位元素，pop（）默认删除最后一位
#list.sort()排序     降序：list.sort(reverse=True)
print(lis1)

#元组
tup=('s',20,[5,9])
tup[1]=200
print(tup)
#元祖中的元素不可变

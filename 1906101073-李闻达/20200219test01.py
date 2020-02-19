a='hi'
b='s'
print(a+b)
#重复字符


c='hi'
print(c*3)

#切片 
str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])


#格式化输出
print("我叫%s"%('张三'))
print("我今年%d"%(10))




#列表
list=[1,2,3,[4,5,6]]
print(len(list))

#迭代
for x in [1,2,3]:
    print(x)


#增加删除
#list.append(7)
#list.extend([1,2])
#print(list)
#print(list.index(2))
#list.pop()
#list.pop(1)
#排序
list=[5,4,2,8,3,8]
list=list.sort()
print(list)



#元组
tup=('s',100,[1,2])
#tup[1]=200  报错，元组中的元素不能更改
print(tup)

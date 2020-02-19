a='hi'
b='s'
print(a+b)


c='hi'
print(c*3)


s='abcde'
print(s[0])
print(s[1])
print(s[0:4])


#格式化输出
print("我叫%s"%('张三'))



#列表
list1=[1,2,3,[4,5,6]]
print(len(list1))
for x in range(len(list1)):
    print(list1)
    



#添加
list1=[1,2,3,[4,5,6]]
list1.append(7)
list.extend([1,2])
print(list1)


#索引
print(list.index(2))
list=list.sort(list)
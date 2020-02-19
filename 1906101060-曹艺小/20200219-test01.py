 


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
print("我今年%d"%('10'))


#列表
lis1=(1,2,3,[4,5,6])
lis1.append(7)
lis1.extend([1,2])
print(lis1.index(2))
lis1.sort()
print(lis1)
print(len(lis1))
for x in range(len(lis1)):
    print(lis1[x])


#元组
tup=('abc',100，[1,7])
tup[1]=200 元组不可更改
print(tup)





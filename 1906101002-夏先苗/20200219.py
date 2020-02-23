#连接
a="hi"
b="s"
print(a+b)

#重复字符
c="hi"
pritn(c*3)

#切片
str1="abcde"
print(str1[0])
print(str1[-1])
print(str1[]0:4)

a="bcde"
print("e" in a)
print("f" not in a)

#格式化输出
print("我叫%s"%("夏先苗"))
print("我今年%s"%(19))

#列表
list1=[1,2,3,[4,5,6]]
print(len(list1))

for x in [1,2,3]:
    print(x)

list1 =[1,2,3,[4,5,6]]
list1.append(7)
list1.extend([1,2])
print(list1.index(2))

list2=[5,4,2,8,3,9]
list2.pop(1)
print(list2)
list2.sort(1)
print(list2)

#元组
tup=("s",100,[1,2])
print(tup)

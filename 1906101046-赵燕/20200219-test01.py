a="hi"
b="s"
print(a+b)

c="hi"
print(c*3)

str1="abcde"
print(str1[0])
print(str1[-1])
print(str1[0:4])

"a="abcd"
print('e' in a)
print('a' in a)
print('e' not in a)

print("我叫%s"%("张三"))
print("我今年%d"%(10))


#列表
list1=[1,2,3,[4,5,6]]
print(len(list1))

for x in [1,2,3,4]:
    print(x)

list=[1,2,3,4,5]
list.append(7)
print(list)
list.extend([1,2])
print(list)
print(list.index(2))
print(list.pop(1))

list=[5,4,2,8,3,8]
list.sort()
print(list)

tup=('s',100,[1,3])
tup[1]=200 #元组元素不能被更改
print(list)
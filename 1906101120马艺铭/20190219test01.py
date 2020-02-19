a='s'
b='a'
print(a+b)

c='hi'
print(c*3)


str1="abcde"
print(str1[0])
print(str1[-1])
print(str1[0:4])  #左闭右开

print("我叫%s"%('张三'))
print("我今年%d"%(10))

#
list=[1,2,3,[4,5,6]]
print(len(list))
for x in [1,2,3]:
    print(list[x])



list=[1,2,3,[4,5,6]]
list.append(7)
list.extend([1,2])
print(list.index(2))

list=[5,4,2,8,3]
list.sort()
print(list)

list=[5,4,2,8,3]
list.pop()
list.pop(1)
print(list)



tuple=('s',100,[1,2])
print(tuple)







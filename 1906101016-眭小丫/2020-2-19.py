a='hi'
b='s'
print(a+b)

c='hi'
print(c*3)

str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])

print("我叫%s"%('张三'))
print("我今年%d"%(10))

list=[1,2,3,[4,5,6]]
print(len(list))
for x in range(len(list)):
    print(list[x])

    list=[5,3,6,8,2,4]
    list.sort()
    print(list)

    tup=('s',100,[1,2])
    tup[1]-200
    print(tup)
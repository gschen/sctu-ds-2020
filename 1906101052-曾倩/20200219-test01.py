a='hi'
b='s'
print(a+b)

c='hi'
print(c*2)

strl='abcde'
print(strl[0])
print(strl[-1])
print(strl[0:3])

print("我叫%s"%('李四'))
print("我今年%d"%(10))

list=[1,2,3,4,[5,6,7]]
print(len(list))

for x in [1,2,3]:
    print(x)
list.append(8)
list.extend([1,2])
print(list.index(2))

list=[1,5,6,4,3,7]
#list.pop()
list.pop(1)
# list.sort()
print(list)

tup=('s',100,[1,2])
#tup[1]-200 不可更改
print(tup)
a='hi'
b='s'
print(a+b)

c='hi'
print(c*3)

str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])


print('我叫%s'%('张三'))
print('我今年%d'%(10))


lis1=[1,2,3,[4,5,6]]
print(len(lis1))

for x in range(len(lis1)):
    print(lis1[x])

lis1.append(7)
print(lis1)

lis2=[5,4,2,8,3,8]
#lis2.append(7)
#lis2.extend([1,2])
lis2.pop()
#lis2.sort()
print(lis2)


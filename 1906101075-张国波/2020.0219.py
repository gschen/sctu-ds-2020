
b='s'
print(a+b)

c='hi'
print(c*3)

strl='abcde'
print(strl[0])
print(strl[-1])
print(strl[0:4])


print('我是%s'%('张三'))



list=[1,2,3,[4,5,6]]
print(len(list))
for x in range(len(list)):
    print(list[x])

list=[1,2,3,[4,5,6]]
#list.append(7)
#list.extend([1,2])
list.pop()
list.sort()
print(list)



tup=('s',100,[1,2])
#tup[1]=200
print(tup)
a='hi'
b='c'
print(a+b)

c='hi'
print(c*3)

str1='abcde'
print(str1[0])
print(str1[-2])
print(str1[0:4])


print('我叫%s'%('张三'))
print('我今年%d'%(20))


lis1=[1,2,3,[4,5,6]]
print(len(lis1))


lis1=[1,2,3,[4,5,6]]
for x in range(len(lis1)):
         print(lis1[x])



lis1=[1,4,9,5,8]
#lis1.append(7)
#lis1.extend([1,7])
lis1.sort()  #排序
lis1.pop()  #删除
print(lis1)


tup=('s',100,[1,7])
#tup[1]=200  元组不可更改
print(tup)
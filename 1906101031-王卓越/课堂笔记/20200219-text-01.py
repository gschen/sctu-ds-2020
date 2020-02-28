a='hi'
b='s'
print(a+b)

c='hi'
print(c*3)

str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:4])

print('b'in str1)
print('b'not in str1)

print("我叫%s"%('王'))#%s为字符串占位符
print('2+5=%d'% 7)#%d为数字占位符

li=[1,2,3,[1,2,3]]
print(li)
li.append(7)
print(li.index(7))
k=1000
li.insert(-1,6)
print(li)

for x in [1,2,3]:
    print(x)

tup=(1,'w',[1,2])
print(tup,type(tup))#元组不支持更改

li=[x for x in range(1,10)]
print(li.pop(3))
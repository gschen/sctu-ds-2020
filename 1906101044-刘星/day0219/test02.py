a='hi'
b='s'
print(a+b)

#重复字符
c='hi'
print(c*3)

str1='abcde'
print(str1[0])
print(str1[-1])
print(str1[0:3])
print('s' in str1)
print('r' not in str1)

#格式化输出
print('我叫%s'%('liuxing'))
print('我今年%d'%(20))

#列表
lis1=[1,2,3,[4,5,6,7]]
print(len(lis1))

#迭代输出
lis1=[1,2,3,[4,5,6,7]]
for x in range(len(lis1)):
    print(lis1[x])

lis1=[1,4,2,8,9,5]
#lis1.append(6)
#lis1.extend([3,7])
lis1.sort( ) #排序
lis1.pop( ) #删除
print(lis1)

#元组
tup=('s',100,[1,7])
#tup[1]=200
print(tup)
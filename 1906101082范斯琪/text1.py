#连接字符
a='hi'
b='s'
print(a+b)

#重复字符
a='hello'
print(a*3)

#切片
strl='abcde'
print(strl[0])
print(strl[-2])
print(strl[0:3])

#格式化输出
print('我叫%s'%('张三'))
print('我今年%d'%(10))

#列表
lis1=[1,2,3,[4,5,6]]
print(len(lis1))            #4（lis1的元素长度）
for x in range(len(lis1)):
    print(lis1[x])

lis1=[1,2,3,[4,5,6]]    
lis1.append(7)              #1,2,3,[4,5,6],7
lis1.extend([1,2])          #1,2,3,[4,5,6],7,1,2
print(lis1.index(2))        #列表中第一个2的位置

lis1=[5,4,2,8,8,3]          
lis1.sort()                 #排序
lis1.pop()                  #删除最后一个
lis1.pop(1)                 #通过下标删值，默认是最后一个
print(lis1)

#元组
tup=('s',100,[1,2])
#tup[1]=200     元组元素不能被更改
print(tup)



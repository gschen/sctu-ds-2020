a="hi"
b="s"
print(a+b)
#重复字符

c='hi'
print(c*3)


strl='abcde'
print(strl[0])
print(strl[-1])
print(strl[0:4])


#格式化输出
print("我叫%s"%('马端浩'))
print("我今年%d"%(18))


#列表
lisl=[1,2,3,[4,5,6]]
print(len(lisl))
for x in range(len(lisl)):
    print(lisl[x])

lisl=[1,2,3,[4,5,6]]
lisl.append(7)
lisl.extend([1,2])
print(lisl.index(2))

lisl=[5,4,6,2,3]
lisl.pop()
#lisl.sort()
print(lisl)
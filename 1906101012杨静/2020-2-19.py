a="hi"
b="s"
print(a+b)
#重复字符

c="hi"
print(c*3)

str1="abcde"
print(str1[0])
print(str1[-1])
print(str1[0:4])


a="bcde"
print("e"in a)
print("f"not in a )


print("我叫%s"%("张三"))
print("我今年%d"%(10))

list1=[1,2,3,[4,5,6]]
print(len(list1))

for x in [1,2,3]:
    print(x)

list1=[1,2,3,[4,5,6]]
list1.append(7)
list1.extend([1,2])
print(list1.index(2))


list2=[5,4,2,8,3,9]
list2.pop(1)
#list2.sort()
print(list2)


tup=("5",100,[1,2])
#tup[1]=200   元组值不会改变
print(tup)
a="he"
b="llo"
c=a+b
print(a+b)
print(c*3)
print(c[1])
print((c*3)[-1])
print(c[1:3])
 
print("你好，%s"%("张三"))
print("今天是%d号"%(19))

list1=[1,2,3,[4,5,6]]
print(len(list1))
list1.append(7)
list1.extend([4,5])
print(list1)

list2=[5,4,8,1,2]
list2.sort()
print(list2)

t=(1,2,[3,4])
t.pop(0)
a  = "hi"
b = "s"
print(a+b)

str1 = "abcdefg"
print(str1[0])
print(str1[-1])
print(str1[0:4])


s = "lucky"
print("a" in s)
print("a" not in s)
print("u" in s)
print("u" not in s)

print("我叫%s"%("张三"))
print("我今年%d岁"%10)



list1= [1,2,3,[4,5,6]]
list1.append(7)
print(list1)

list2 = [5,6,8,1,3,7,9]
list2.sort()
list3 = sorted(list2)
print(list2)
print(list3)


tuple=("s",2,4)
# tuple[1] = 5 元组不能修改元素
print(tuple[1])
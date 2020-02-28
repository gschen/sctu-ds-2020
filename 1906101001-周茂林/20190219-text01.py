a = 'h'
b = 'i'
print(a+b)

c = 'ee'
print(c*5)


s1 = 'qwertty'
print(s1[3])
print(s1[2:4])

print('q' in s1)

print('他叫%s' % ('老六'))
print('他%s岁了' % (19))

#列表
list1 = [1, 2, 3, [4, 5, 6]]
print(len(list1))
list1.append(7)
print(list1)
list1.extend([1, 2])
print(list1)
print(list1.index(1))

list2 = [4, 1, 6, 5, 2, 3]
list2.sort()
print(list2)

#迭代
for i in [1, 2, 3]:
    print(i)

#元组
tup1 = ('a', 12, [1, 2])
print(tup1)

#tup[1]=200  会报错
"+号，字符串的连接"
a = "hi"
b = "s"
print(a+b)
"重复字符*"
c = "hi"
print(c*3)
"索引[]"
str1 = "abcde"
print(str1[0])
print(str1[-1])
"多字符切片"
print(str1[0:4])
"用in判断是否存在"
print("a" in str1)
"用not in判断不存在"
print("v" not in str1)
"格式化输出"
print("我叫%s"%("卢本伟"))
print("我进年%d岁"%(10))

#列表
list1 = [1,2,3,[4,5,6]]
print(len(list1))
#组合用+号
#重读用*
#存在用in

#迭代
for i in [1,2,3,4]:
    print(i)
#增加
list1 = [5,4,2,8,3,8]
#list1.append(7)
#list1.extend([1,2])
list1.pop(1)
#list1.sort()  排序
print(list1)

#元组 
tup = ("s",100,[1,2])
tup[1] = 200 #元素不可修改
print(tup)


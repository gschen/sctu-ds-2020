a='hi'
b='s'
print(a+b)
#重复字符
c='hi'
print(c*4)
#字符切片
str='apple'
print(str[1])
print(str[-1])
print(str[0:4])
#格式化输出
print('我的名字是%s'%('dj'))
print('我今年%d'%(20))
#列表
list=[1,2,3,4,[5,6,7]]
print(len(list))
for x in range(len(list)):
    print(list[x])
#用not in 判断不存在
#print("v" not in str1)
#添加
list=[1,3,[4,5,6]]
list.append(8)
list.extend([1,2])
print(list)
#索引
list=[1,2,3,4,5,6]
print(list.index(3))
#排序
list.sort()
print(list)
#元祖
tup=('s',10,[1,2])
print(tup)
#tup[1]=100,元祖里的元素不可修改
#print(tup)



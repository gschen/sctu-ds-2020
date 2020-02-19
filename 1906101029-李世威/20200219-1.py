a="hi"
b="s"
print(a+b)    
 # 重复字符
c="b"
print(c*6)
# # 切片
d="qwer"
print(d[2])
print(d[0:2])

# 格式化输出
print("你是%s"%"张三")
print("我%d岁"%(18))
print("你是%s,你%d岁"%("张三",18))



# 列表
list=[1,3,2,4,5]
# list.append(4)
# list.extend([1,3])
# list.pop(1)通过下标，默认删除最后一个
# sorted有返回值，sort没有返回值
print(sorted(list))
list.sort()
print(list)
for i in [1,2,3]:
     print(i)
   



# 元组
w=("sa",16,[1,2,"t"])
print(w)

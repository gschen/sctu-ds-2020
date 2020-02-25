#构建集合
#两种方法
A = {"a","b","c","c",1} #然后每个元素用逗号隔开，字符串类型的数据需要加定界符。
B = set("aabbcce")#注意使用的是小括号，所有元素放在一起，

#print(A,b)

#集合的并集
#print(A|B)
#集合的交集&
#print(A&B)
#集合的补集
#print(A-B)#A当作全集，B当作补集
#不同时包含
#print(A^B)

#集合的增删
#两种方法
#A.add('d')#元素存在时不操作
#print(A)
#B.update({1,3},[4,2],"e")#元素可以多种多样
#print(B)


#删除元素的方法

#A.remove("a")#删除不存在的元素会报错
#A.discard("f")#元素不存在也不会报错
#A.pop()#随机的删除一个元素
#print(A)

#字典

dic = {"name":"张三","age":19,"school":"sctu"}

#修改数据
dic["name"] = "李四"
#print(dic)

#查找数据
#print(dic.get("name"))#返回指定键的值，不存在则返回default值

#dic.setdefault("address","成都")#返回一个值，不存在则新建
#dic.setdefault("name")

#增加数据
#dic["class"] = "1班"
#print(dic)

#删除数据
#del dic["name"] 删除指定键
#dic.pop("age") #必须给定键值，并返回键值

#dic.popitem()#直接删除最后一个值并返回


#python函数

#def
# def AplusB(a,b):
#     return a+b
# result=AplusB(1,2)
# print(result)

# def mj(r,pi):
#     area = r**2*pi
#     return area
# print(mj(6,3.14))
# print(mj(pi = 3.14,r = 6))

# a = 2
# def main():
#     b=3
#     print(a)
# main()
# print(b)

#lambda匿名函数

# circle = lambda r,pi:r**2*pi
# print(circle(3,3.14))

# def change(a):
#     a = 10
# b = 2
# change(b)#2 > a,a = 2 > a=10
# print(b)

# c = [1,2,3]
# def change2(x):
#     x.append([1,2,3])
# change2(c)
# print(c)

def main(x,*y):
    print(x)
    print(y)
main(1,11,12,13,14)
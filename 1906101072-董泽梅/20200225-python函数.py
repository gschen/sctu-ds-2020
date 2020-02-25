#python函数
# def hs(a,b):
#     return a+b
# result=hs(2,3)
# print(result)

#实例
#传入一个参数半径r，计算圆的面积

# def area(r):
#     s=3.14*r**2
#     return s
# s = area(3)
# print(s)

#形参和实参
#形参
# def area(r):
#     s = r**2*3.14
#     return s

#实参
# def area(r=6):
#     s = r**2*3.14
#     return s

# def abc(r,pi):
#     s = r**2*pi
#     return s
# print(abc(6,3.14))
# print(abc(r=6,pi=3.14))


#lambda函数
# circle = lambda r,pi:r**2*pi
# print(circle(3,3.14))

#python传不可变对象实例
# def chage(a):
#     a = 10
# b = 2#此时传入的是2不是b，a=2,然后a又被赋值为10.b依然为2
# chage(b)#相当于b=a
# print(b)

#python传入可更改对象
# c=[1,2,3]
# def chage2(x):
#     x.append([1,2,3])
# chage2(c)
# print(c)


#不定长参数
# def printinfo(x,*y):
#     print(x)
#     for i in range(len(y)):
#         print(y[i])
# printinfo(1,11,12,13,14,15)
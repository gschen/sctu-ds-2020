# 函数的定义

# def ApluaB(a,b):
#     return a+b
# print(ApluaB(2,4))
# result=ApluaB(1,2)
# print(result)

# 求圆的面积

# def s(r):
#     return r**2*3.14
# print(s(3))

# def s(r,pi=3.14):     # 形参写在实参前面
#     return r**2*pi
# print(s(2))

# def c(r=5,pi=3.14):
#     area=r**2*pi
#     print(area)
# c()


# a=2     # 全局变量
# def main():
#     b=3     # 局部变量不被函数调用
#     print(a)
# main()
# print(b)    
# 结果a=2，b没有被定义


# lambda函数
# circle=lambda r,pi:r**2*pi
# print(circle(2,3.14))

# def changeint(a):
#     a=10
# b=2
# changeint(b)
# print(b)
# 结果为2

# l=[0]
# def change(x):
#     return x.append([1,2,3])
# change(l)
# print(l)

# def main(x,*y):
#     print(x)
#     for i in range(len(y)):
#         print(y[i])
# main(1,'a','b',2,3)


# def AplusB(a,b):
#     return a + b
# print(AplusB(2,4))
# result = AplusB(1,2)
# print(result)


# 圆面积
# def S(r):
#     return r**2*3.14
# print(S(5))

# def S(r,pi=3.14):  # 形参写在实参前
#     return r**2*pi
# print(S(5))

# def circle(r=5,pi=3.14):
#     area = r**2*pi
#     print(area)
# circle()



# a = 2       # 全局变量
# def main():
#     b = 3   # 局部变量不被函数调用
#     print(a)
# main()
# print(b)


# lambda函数
# circle = lambda r,pi:r**2*pi
# print(circle(5,3.14))


# def ChangeInt(a):
#     a = 10
# b = 2
# ChangeInt(b)
# print(b)


# l = [0]
# def change(x):
#     return x.append([1,2,3])
# change(l)
# print(l)


# def main(x,*y):
#     print(x)
#     for i in range(len(y)):
#         print(y[i])

# main(1,'a','b',1,2)



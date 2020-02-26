#函数


# def Aplus(a,b):
#     return a+b
# result=Aplus(1,2)
# print(result)
# print(Aplus(8,9))


# def zhou(r):
#     return r**2*3.14
# a=int(input("请输入一个半径："))
# print(zhou(a))


#传入参数顺序：形参在实参之前
# def zhou(r,pi):
#     return r**2*pi
# a=int(input("请输入一个半径："))
# print(zhou(a,3.14))


# a=2
# def main():
#     b=3
#     print(a)
# main()
# print(b)


# circle=lambda r,pi:r**2*pi
# print(circle(4,3.14))

#str,tuple和numbers为不可更改对象
#list，dic为可更改对象


# def change(a):
#     a=10
# b=2
# change(b)
# print(b)


# c=[1,2,3]
# def change2(x):
#     x.append([1,2,3])
# change2(c)
# print(c)


# def main(x,*y):
#     print(x)
#     for i in y:
#         print(y)
# main(1,11,12,13,14)
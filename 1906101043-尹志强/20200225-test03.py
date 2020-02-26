# def AplusB(a,b):
#     c=a+b
#     return c
# result=AplusB(2,3)
# print(result)



# def circle(r):
#     a=r**2*3.14
#     return a
# print(circle(2))


# a=2
# def main():
#     b=3
#     print(a)
# main()
# print(b)#(b并不存在，因为函数内的变量不能调用)



# #匿名函数lambda
# circle=lambda r,pi:r**2*pi
# print(circle(3,3.14))

#不可更改对象
# def change(a):
#     a=10
# b=2
# change(b)
# print(b)#(传得是b的值不是b本身)

##可更改对象
# c=[1,2,3]
# def change1(x):
#     x.append([1,2,3])
# change1(c)
# print(c)


# def main(x,*y):
#     print(x)
#     print(y)

# main(1,11,12,13,14)


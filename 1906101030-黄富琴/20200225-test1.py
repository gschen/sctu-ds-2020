# def AplusB(a,b):

#     return a+b
# result=AplusB(1,2)
# print(result)
# print(AplusB(10,12))

# def mianji(r):
#     return r**2*3.14
# print(mianji(3))

# #命名空间
# a=2
# def main():
#     b=3
#     print(a)
# main()
# print(b)

# #匿名函数Lambda
# circle=lambda r,pi:r**2*3.14
# print(circle(3,3.14))

# #传不可变对象
# def ChangeInt(a):
#     a=10

# b=2
# ChangeInt(b)
# print(b)

# #传可变对象
# c=[1,2,3]
# def ChangeInt1(x):
#     x.append([1,2,3])
# ChangeInt1(c)
# print(c)


def main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])

main(1,7,8,9,10)
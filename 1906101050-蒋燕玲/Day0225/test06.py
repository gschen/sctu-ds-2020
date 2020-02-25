# def s(r):
#     s=3.14*r**2
#     return s
# print(s(2))



# def s(r,pi):
#     s=r**2*pi
#     return s
# print(s(6,3.14))
# print(s(pi=3.14,r=6))#形参在实参前面


#局部空间内可以访问全局变量，全局空间内不可以访问局部变量
# a = 2
# def main ():
#     b = 3
#     print(a)
# main()
# print(b)


#Lambda(匿名函数)
#s=lambda r,pi:r**2*pi
#print(s(3,3.14))


# def chenge(a):
#     a = 10
# b = 2
# chenge(b)#2-a 传入的是值 a = 2-->a=10
# print(b)#=2

# #不可更改，字符串，元祖，数字  传入本身和数值
# c=[1,2,3]
# def change1(x):
#     x.append([1,2,3])
#     change1(c)
# print(c)



#不定长参数 加一个*
def main(x,*y):
    print(x)
    #print(y)
    for i in len(y):
        main(1,112,13,15)

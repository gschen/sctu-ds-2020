# def AplusB(a,b):

#     return a+b 
# result=AplusB(1,2)
# print(result)
# print(AplusB(10,12))


# def s(r):
#     return r**2*3.14
# x=int(input('请输入一个数字'))
# print(s(x))

# def s(r,p):
#     aera=r**2*p
#     return aera
# print(s(2,3.14))

# s=lambda r,p:r**2*p
# print(s(2,3.14))


def main(x,*y):
    print(x)
    for i in y:
        print(y)

main(1,11,12,13,14)
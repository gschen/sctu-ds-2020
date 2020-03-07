#类（代码和函数的封装体）

# class Test():
#     def original(self):
#         lis=[chr(i) for i in range(97,123)]
#         print("".join(lis))
#     def overturn(self):
#         print("".join([chr(i) for i in range(98,64,-1)]))
# a=Test()
# a.original()   
# a.overturn()   

# class Test():
#     def __init__(self,a,b):
#         print("已运行",a+b)
# a=Test(10,20)

# b=list([1,2,3])
# print(b)


# class Test():
#     b=12
#     def __init__(self):
#         self.c=12
# a=Test()
# print(a,b,a,c)


class Test1():
    def __init__(self):
        self.x=[1,2,3] #实例变量


class Test2():
    x=[1,2,3] #类变量
#test01
a=Test1()
b=Test1()
a.x.append("abc")
print("test01",a.x,b.x)

#test02
c=Test2()
d=Test2()
c.x.append("cde")
print("test02",c.x,d.x)
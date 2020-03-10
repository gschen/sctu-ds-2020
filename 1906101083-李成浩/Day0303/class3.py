# class Test():
#     a = 1
#     def __init__(self,a=a):
#         print("已经运行",a+b)    类变量

# a = Test(10,20)

class Test():
    x = [1,2,3]
a = Test()
b = Test()
a.x.append([1,2,3])
print(a.x,b.x)



#实例变量
# class Test():
#     def __init__(self):
#         self.x = [1,2,3]
# a = Test()
# b = Test()
# a.x.append([1,2,3])
# print(a.x,b.x)

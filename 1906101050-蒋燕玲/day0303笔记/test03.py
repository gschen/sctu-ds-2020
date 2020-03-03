# 类的标准写法
# :class Test()
     #def _init_(self,a,b):#实例化时传入参数咋子这
            #定义变量在此处
            #self.x=a
            #self.y=b
            #self.xx....
#         print("已运行",a+b)
# a=Test(10,20)

# b=list([1,2,3])
# print(b)


class Test2():
   x=[1,2,3]#类变量 对象共用


class Test1():
  def __init__(self):
      self.x=[1,2,3]#实例变量

#test01
a=Test1()
b=Test1()
a.x.append('abc')
print("test02",a.x,b.x)



#test02
c=Test2()
d=Test2()
c.x.append('abc')
print("test02",c.x,d.x)

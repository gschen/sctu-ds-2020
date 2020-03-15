#类


#类里面的变量统称为属性
class MyClass:
    i = 12345  #类变量
    def f(self):    #函数必须是self
        return "hello,world"    #实例化类
x = MyClass()    #访问类的属性和方法（创建一个MyClass类的对象x）
print("MyClass 类的属性i为：",x.i)    # x.i 访问对象属性即类变量
print("MyClass 类的方法f输出为：",x.f())


#类的标准写法


class Myclass():
    def __init__(self,a,b):#实例化时传入参数
        #定义变量
        self.x=a
        self.y=b
        #self.xxx........
        #也可以写一些在实例化时便要执行的操作

    #定义函数往后
    def f1(self):
        #如果要调用实例变量 --> self.变量名
        c=self.x+self.y
        return c
    def f2(self):
        pass 
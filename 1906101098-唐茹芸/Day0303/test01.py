#类


#类里面的变量统称为属性
class MyClass:
    i = 12345  #类变量
    def f(self):    #函数必须是self
        return "hello,world"    #实例化类
x = MyClass()    #访问类的属性和方法（创建一个MyClass类的对象x）
print("MyClass 类的属性i为：",x.i)    # x.i 访问对象属性即类变量
print("MyClass 类的方法f输出为：",x.f())



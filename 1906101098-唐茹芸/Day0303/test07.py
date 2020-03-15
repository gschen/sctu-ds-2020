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
#test01
a = test1()
b = test1()
axappend('abc')
打印('test01'，ax，bx)
#test02
a = Test2（） 
b = Test2（） 
axappend（'cde'）
打印（'test02'，ax，bx）
'''
＃类的标准写法
'''
classMyclass（）：
    def __init __（self，a，b）：＃实例化时试图参数在这
    ＃定义变量在此处
        self.x = a
        self.x = b
    ＃self.xxx .....
    ＃也可以写一些在实例化时便要执行
    ＃定义函数后
    def f1（self）：
        ＃如果要调用实例变量-> self。变量名
        c = self.x + self.y
        返回c
    def f2（self）：
        通过    
'''
＃类的继承
'''
class parent（）：
    def __init __（）：
        self.p ='我是父类'
    def f（）：
        print（'财产1w'）
班级儿童（父母）：
    def __init __（）：
        self.q ='我是子类'
    def t（）：
        打印（self.q，'我要继承'）
a = child（）
在（）
af（）
'''
＃私有公有
'''

    def __init __（）：
        自我.__ x = 1
        self.y = 2
    def __f（）：
        print（'这是密码'）    
a = test（）
打印（是）
打印（ax，a .__ x）
af（）
a .__ f（）
'''
'''
#class Test01（）：
    def __init __（）：
        self.t1 ='我是父类'
    def f（）：
        返回“爸爸”
Test02（）类：
    def __init __（）：
        self.t2 ='我是子类'
    def f（自我，对象）：
        打印（object.f（））
a = Test01（）
def main（对象）：
    打印（object.f（））
    返回“ 123”
#print（main（a））
＃类的标准写法
类 Myclass（）：
    def  __init__（self，a，b）：＃实例化时初始化参数在这
        ＃定义变量在此处
        自我。x = a
        自我。y = b
        ＃self.xxx .....
        ＃也可以写一些在实例化时可以执行的操作

    ＃定义函数往后
    def  f1（self）：
        ＃如果要调用实例变量-> self。变量名
        c = 自我。x + 自我。ÿ
        返回 c
    def  f2（self）：
        通过
# 类作为参数传递
#  Test1 类：
    def  __init__（self）：
        自我。t1 = '我是父类'
    def  f（self）：
        返回 “爸爸”

#  Test2 类：
    def  __init__（self）：
        # 自我。t2 = '我是子类'
    def  f（self，object）：#object用于预设参数，作为一个类
        打印（'这是我'，对象。˚F（））

a = Test1（）
b = Test2（）
b=f（a）

def  main（object）：
    # 打印（对象。˚F（）） ＃把一个对象作为参数传到函数里
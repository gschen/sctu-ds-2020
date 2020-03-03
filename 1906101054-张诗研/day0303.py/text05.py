class Text1():
    def __init__(self):
        self.x=[1,2,3]#实例变量

class Text2():
    x=[1,2,3]  #类变量  

a=Text1()  
b=Text1() 
a.x.append("abc")
print("text01",a.x,b.x)

c=Text2()  
d=Text2() 
c.x.append("dfg")
print("text02",c.x,d.x)
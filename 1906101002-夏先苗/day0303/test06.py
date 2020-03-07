#私有公有
class Site:
    def __init__(self,name,url):
        self.name=name
        self.__url=url
    def who(self):
        print('name:',self.name)
        print('url:',self.__url)
    def __foo(self):
        print('这是私有方法')
    def foo(self):
        print('这是公有方法')
        self.__foo()
x=Site('菜鸟教程','www.runoob.com')
x.who()
x.foo()
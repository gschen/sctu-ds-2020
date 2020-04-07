class StackNode:
    def __init__(self):
        self.data = None
        self.next = None
class LinkStack:
    def __init__(self):
        self.top = StackNode()
    '''判断链栈是否为空'''
    def IsEmptyStack(self):
        if self.top.next == None:
            return True
        else:
            return False
    '''进栈'''
    def PushStack(self,da):
        tStackNode = StackNode()
        tStackNode.data = da
        tStackNode.next = self.top.next
        self.top.next = tStackNode
        print("当前入栈的元素为：",da)
    '''出栈'''
    def PopStack(self):
        if self.IsEmptyStack() == True:
            return
        else:
            tStackNode = self.top.next
            self.top.next = tStackNode.next
            return tStackNode.data
    '''获取栈顶元素'''
    def GetTopStack(self):
        if self.IsEmptyStack() == True:
            return
        else: 
            return self.top.next.data
    '''反向输出链栈元素'''
    def ReverseStackTraverse(self):
        list1 = []
        tStackNode = self.top.next
        while tStackNode != None:
            result = self.PopStack()
            list1.append(result)
            tStackNode = tStackNode.next
        for i in list1[::-1]:
            print(i,end = ' ')
class TestBM:
    def BracketMatch(self,str1):
        Ls = LinkStack()
        i = 0
        while i < len(str1):
            if str1[i] == '{':
                Ls.PushStack(str1[i])
                i = i+1
            elif str1[i] == '}':
                if Ls.GetTopStack() == '{':
                    Ls.PopStack() 
                    i = i+1
                else:
                    Ls.PushStack(str1[i])
                    i = i+1
            else:
                 i = i+1
        if Ls.IsEmptyStack() == True:
            print("括号匹配成功！！！")
        else:
            print("匹配失败！！！")
            print("未匹配的括号为：",end = ' ')
            Ls.ReverseStackTraverse()
    
TBM = TestBM()
TBM. BracketMatch("{{{{{}}}}}")


ls = LinkStack()
print(ls.IsEmptyStack())
ls.PushStack(1)
ls.PushStack(2)
print(ls.IsEmptyStack())
print(ls.GetTopStack())
ls.ReverseStackTraverse()
print(ls.PopStack())
print(ls.GetTopStack())
print(ls.PopStack())
print(ls.GetTopStack())
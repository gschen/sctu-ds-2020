class Stack(object):          #定义一个栈
    def __init__(self):
        self.__list__ = []      #栈的容器为list
    def push(self,date):            #压栈的方法
        self.__list__.append(date)    #压栈就是向栈容器list中末尾添加元素
    def pop(self):       #弹出栈顶元素的方法
        return self.__list__.pop()   #出栈就是删掉栈容器list的末尾元素并输出(return)
    def peek(self):     #查看栈顶元素的方法
        return self.__list__[-1]   #与出栈不同，只是查看，不删除
    def add(self):     #为了计算总得数，定义一个对栈容器list求和的方法
        return sum(self.__list__)    #直接对self.__list__用sum函数求和
s = Stack()   #初始化栈为s
score_list = list(map(str,input().split()))  #格式输入得分情况表，如：5 2 C D +
for i in score_list:  #遍历得分情况表的每一个元素
    score = 0    #开始每一次循环时，当局得分(socre)都为0 
    if i == "+":    #如果得分情况为+
        score_1 = s.pop()   #用score_1表示第前一轮得分
        score_2 = s.pop()   #用score_2表示第前两轮的得分
        score += score_1+score_2  #此时本轮得分(score)为前两轮得分和(score_1+score_2)
        s.push(score_1)   #因为前面用了pop()出栈，所以要按顺序将score_1和score_2压回栈
        s.push(score_2)
        s.push(score)   #将本轮得分压如栈
    elif i == "D":    #如果得分情况为D
        score = s.peek()*2   #此时本轮得分就为上轮的得分(栈顶元素)*2
        s.push(score)  #将本轮得分压入栈(因为使用的是peek()函数，所以栈顶没被弹出)
    elif i == "C":  #如果得分情况为C
        s.pop()  #直接弹出上一轮得分(栈顶元素)即可
    else:   #如果上述都不满足，则得分情况就是数字，代表本轮得分
        s.push(int(i))  #注意，输入的得分情况表都是以字符串(str)形式输入的，所以压栈时要用int()转化为数字
print(s.add())  #最后直接调用栈中方法add,输出总得分


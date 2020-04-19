class Queue:
    #初始化队列
    def __init__(self):
        self.que = []
        self.size = 0
    #判断队列是否为空
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    #添加元素
    def enqueue(self,value):
        self.size += 1
        self.que.append(value)
    #删除元素
    def defqueue(self):
        if self.size == 0:
            print('There is nothing')
            return
        else:
            self.size -= 1
            self.que.pop(0)
queue = Queue()
        
        
        
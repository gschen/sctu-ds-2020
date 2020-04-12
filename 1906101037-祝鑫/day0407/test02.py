class Queue:
    #初始化队列
    def __init__(self):
        self.que=[]
        #列表的长度
        self.size=0
      
    #判断队列是否为空
    def is_empty(self):
        if self.size == 0:
            return True
        return False

    #返回队列的长度
    def que_size(self):
        return self.size

    #列表添加元素
    def enqueue(self,value):
        self.size += 1
        self.que.append(value)

    #删除队列元素
    def dequeue(self):
        if self.size == 0:
            print("啥都没有，不能删！")
            return
        else:
            self.size -= 1
            self.que.pop(0)


queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print(queue.que_size())
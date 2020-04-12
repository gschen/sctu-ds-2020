class Queue:
    #初始化队列
    def __init__(self):
        self.que=[]
        self.size=0#列表的长度
    #判断队列是否为空
    def is_empty(self):
        if self.size==0:
            return True
        return False
    #返归对了的长度
    def que_size(self):
        return self.size
    #列表添加元素
    def enqueue(self,value):
        self.que.append(value)
        self.size+=1
    #删除队列元素
    def dequeue(self):
        if self.size==0:
            print('没东西，不能删')
            return
        else:
            self.que.pop(0)
            self.size-=1

queue=Queue()
print(queue.que_size())
print(queue.is_empty())
queue.enqueue(4)
queue.enqueue(6)
print(queue.que_size())
print(queue.dequeue())
print(queue.que_size())

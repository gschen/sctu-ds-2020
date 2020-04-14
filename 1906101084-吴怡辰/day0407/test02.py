# 队列
class Queue:
    # 初始化队列
    def __init__(self):
        self.que = []
        self.size = 0
    # 判断队列是否为空
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    # 返回队列长度
    def que_size(self):
        return self.size
    # 添加元素
    def enqueue(self,val):
        self.size += 1
        self.que.append(val)
    # 删除元素
    def dequeue(self):
        if self.size == 0:
            print('队列为空，不可删')
            return
        else:
            self.size -= 1
            self.que.pop(0)

queue = Queue()
queue.que_size()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(7)
queue.is_empty()

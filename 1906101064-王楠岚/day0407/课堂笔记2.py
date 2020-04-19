# 队列
class Queue:
    # 初始化队列
    def __init__(self):
        self.que = []
        self.size = 0  # 列表的长度

    # 判断队列是否为空
    def is_empty(self):
        if self.size == 0:
            return True
        return False

    # 返回嘟列的长度
    def que_size(self):
        return self.size

    # 列表添加元素
    def enqueue(self, value):
        self.size += 1
        self.que.append(value)

    # 删除队列元素
    def dequeue(self):
        if self.size == 0:
            print('买东西系，不能删')
            return
        else:
            self.size -= 1
            self.que.pop(0)  # 删掉0是栈，加0是队列


queue = Queue()
queue.enqueue(1)
print(queue.que_size())



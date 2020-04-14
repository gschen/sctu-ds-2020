# coding=utf-8

'''队列'''
# 特点:先进先出

class Queue:
    # 初始化队列
    def __init__(self):
        self.que=[]
        self.size=0 # 列表的长度

    # 判断队列是否为空
    def is_empty(self):
        return self.size==0

    # 返回队列的长度
    def que_size(self):
        return self.size

    # 列表添加元素
    def enqueue(self,value):
        self.que.append(value)
        self.size+=1

    # 删除队列元素
    def dequeue(self):
        if self.is_empty():
            print('没东西，删不了')
        else:
            self.que.pop(0)
            self.size-=1

    # 打印队列
    def print_queue(self):
        print(self.que)

queue=Queue()
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.is_empty())
queue.print_queue()
queue.dequeue()
queue.print_queue()
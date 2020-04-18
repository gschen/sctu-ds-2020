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
    #返回队列的长度
    def que_size(self):
        return self.__size
    
    #列表添加元素
    def enqueue(self,value):
        self.size+=1
        que=Node(value)#创建节点
        if self.head is None:#判断是否存在头节点
            self.head = self.end=que
        else:#如果存在头节点
            self.end.next=que#将新节点放在尾节点后面（第一步）
            self.end=que#将尾节点指针指向新节点(第二步)

    #删除队列元素
    def dequeue(self):
        #判断队列是否为空
        if self.head is None:
            print("000")
            return
        else:
            self.size-=1
            self.head=self.head.next#删除元素，使头指针指向下一
            #如果删除元素后，队列没有元素，head此时为None，end此
            if self.head is None:
                self.end=None


queue=Queue()


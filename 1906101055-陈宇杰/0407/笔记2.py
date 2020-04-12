class Queue :
      #初始化队列
      def_init_ (se1f):
        seIf .que=[]
        self . size=8#列表的长度
      #判断队列是否为空
      def is empty(self):
      if self . sIze==0:
               return True
        return False


      #返回队列的长度
      def que_ size(self):
          return self .size
      #列表添加元素
      def enqueue(self,value):
          self. size+=1
          self. que . append(value)

      #删除队列元素s、
      def dequeue(self):
          if self.size--B:
              print("没东西，不能删“)
              return
          else:
               self . size-=1
               self .que . pop(e)
queue=Queue()

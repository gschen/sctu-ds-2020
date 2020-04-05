class Node:
    def __init__(self,value):
        self.value=value#当前节点的值
        self.next=None#下一个节点
class Find:
    #获取链表的长度
    def Find_m(self):
        #cur游标，表示当前操作的节点
        cur=self.__head

        #统计有多少节点
        count=0

        #先判断再加值
        while cur.next!=None:
            count+=1

            #将cur替代为下一个节点
            cur=cur.next
        

        
        if count % 2==1:
            i=(count+1)/2         
        else:
            i=count/2+1
        cur=self.__head
        while i:
            cur=cur.next
            i=i-1
        return cur
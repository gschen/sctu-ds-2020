class Node:
    def __init__(self,value):
        self.value=value#当前结点的值
        self.next=None#下一个结点

class List():
    def __init__(self):
        #头结点
        self.head=Node(1)
    #头插法创建单链表
    def insert_before(self,date):
        for i in date:
            node=Node(i)#创建新结点
            #判断头结点的下一个结点是否为空
            if self.head.next is None:#如果为空则将新结点加入到next
                self.head.next=node
            else:
                node.next=self.head.next#将头结点的下一个结点加入到当前结点的next
                self.head.next=node
    #尾插法创建单链表
    def insert_tail(self,date):
        tail=self.head.next
        for i in date:
            node=Node(i)
            if tail is None:
                self.head.next=node
                tail=node
            else:
                tail.next=node
                tail=node
    #打印单链表
    def list_print(self):
        node=self.head.next
        while node:
            print(node.value,' ',end='')
            node=node.next
        print('')
    #删除列表的重复元素
    def clear_repetition(self):
        cur=self.head
        while cur:
            while cur.next and cur.next==cur.next.value:
                cur.next=cur.next.next
            cur=cur.next
    #获取链表的长度
    def length(self):
        #cur游标，表示当前操作的节点
        cur=self.head
        #统计有多少节点
        count=0
        while cur!=None:
            count+=1
            #将cur替换为下一个节点
            cur=cur.next
        return count

    def list_element_add(self,i,value):
        node_new=Node(value)#创建新结点
        index=0
        node=self.head.next
        while node:#找位置
            index=index+1
            if index==i-1:
                break
            node=node.next
        if node is None:
            return False
        node_new.next= node.next#插入结点
        node.next=node_new




if __name__=='__main__':
    s1=List()
    s1.insert_tail('4')
    s1.insert_tail('4')
    s1.insert_tail('8')
    s1.insert_before('6')
    # print(s1.length())
    print(s1.list_print())


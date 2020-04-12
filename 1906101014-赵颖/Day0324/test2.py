#给定一个不为空的链表，要求找到该链表的中间节点(若有两个中间值取第二个)，然后输出中间值往后的链表
#例如：[1,2,3,4,5]
#输出：[3,4,5]
class Node:
     def __init__(self,value):
         self.value=value#当前结点的值
         self.next=None#下一个结点
 class Listzj():
     def __init__(self):
         self.head=Node(1)
     def insert_before(self,date):
         for i in date:
             node=Node(i)
             if self.head.next is None:
                 self.head.next=node
             else:
                 node.next=self.head.next
                 self.head.next=node
     def length(self):
         node=self.head
         cur=self.head
         count=0
         while cur!=None:
             count+=1
             node=node.next
         return count
         if count%2==0:
             for k in ((count/2)+1):
                 cur=cur.next
             while node:
                 print(node.value,' ',end='')
                 node=node.next
             print('')
         else:
             for k in ((count+1)/2):
                 cur=cur.next
             while node:
                 print(node.value,' ',end='')
                 node=node.next
             print('')
 if __name__=='__main__':
     s1=Listzj()
     print(s1.length())
     s1.insert_before('5')
     s1.insert_before('4')
     s1.insert_before('3')
     s1.insert_before('2')
     s1.insert_before('1')
     print(s1.length())

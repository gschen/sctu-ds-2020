#尾插法创建单链表
def insert_ tail(self ，data):
tai l=self . head . next
for i in data:
node=Node( i)
ArA
if tail is None:
self . head. next = node
tail = node
else :
tail.next = node
tai l=node









def list element. add(selfaduvalue);
node_ new-Node (value)创建新节点
index=0
A
node=self. head. next
while node:#找位置
index= index+1
if index == i-1 :
break
白
node=node. next
if node is None :
return False
node_ new. next=node. next插入节点
白
node. next=node. new

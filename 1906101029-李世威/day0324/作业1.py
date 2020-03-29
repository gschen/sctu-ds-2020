class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
n1 = Node('1',None)
n2 = Node('2',n1)
n3 = Node('3',n2)
n4 = Node('4',n3)
n5 = Node('5',n4)
n6 = Node('6',n5)
n7 = Node('7',n6)

p1 = n7
p2 = n7
while p2.next is not None and p2.next.next is not None:
    p1 = p1.next
    p2 = p2.next.next
print(p1.data)
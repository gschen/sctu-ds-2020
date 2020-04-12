# 在第i个节点前插入值为value的节点
def list_element_add(self, i, value):

    node_new = Node(value)#创建新节点

    index = 0
    node = self.head.next

    while node:#找位置
          index = index + 1
        
          if index == i - 1:
            break

          node = node.next

    if node is None:
        return False

    node_new.next = node.next#插入节点
    node.next = node_new 
class Node(object):
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.item)

class Tree(object):
    def __init__(self):
        self.root = Node('root')
    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                elif pop_node.right is None:
                    pop_node.right = node
                    return 
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def insertLeft(self,item):
        node = Node(item)
        if self.root.left is None:
            self.root.left = node
        else:
            node.left = self.root.left
            self.root.left = node
    def insertRight(self,item):
        node = Node(item)
        if self.root.right is None:
            self.root.right = node
        else:
            node.right = self.root.right
            self.root.right = node

    def get_parent(self,item):
        if self.root.item == item:
            return None
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            if pop_node.left and pop_node.left.item == item:
                return pop_node
            if pop_node.rignt and pop_node.rignt.item == item:
                return pop_node
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)

    def delete(self,item):
        if self.root is None:
            return False
        parent = self.get_parent(item)
        if parent:
            del_node = parent.left if parent.left.item == item else parent.right
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.left
                del del_node
                return True
            elif del_node.right.item == item:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.left = tmp_next
                del del_node
                return True
        return False

t=Tree()
t.add(1)
t.add(2)
t.add(3)
t.add(4)
print(t.get_parent(3))
t.delete(1)
print(t.get_parent(4))
print(t.get_parent(3))
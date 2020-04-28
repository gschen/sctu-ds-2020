class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        # print 一个Node类时会打印_str_的返回值
        return str(self.item) 


class Tree(object):
    def __init__(self):
        # 根结点定义为root 永不删除
        self.root = Node("root")

    def add(self, item):
        node = Node(item)
        # 如果二叉树为空，那么生成的二叉树最终为新插入
        if self.root is None:
            self.root = node
        else:
            # 将q列表添加二叉树的根结点
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                # 如果左子树为空，则将该点添加到左子树
                if pop_node.left is None:
                    pop_node.left = node
                    return
                # 右子树为空则将点添加到右子树
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def insertLeft(self, item):
        node = Node(item)
        if self.root.left is None:
            self.root.left = node
        else:
            node.left = self.root.left
            self.root.left = node

    def insertRight(self, item):
        node = Node(item)
        if self.root.right is None:
            self.root.right = node
        else:
            node.right = self.root.right
            self.root.right = node

    def get_parent(self, item):
        if self.root.item == item:
            # 根结点没有父结点
            return None
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            # 某一点的左子树为寻找的点
            if pop_node.left and pop_node.left.item == item:
                # 返回某点，就是寻找的父结点
                return pop_node
            # 某一点的右子树为寻找的点
            if pop_node.right and pop_node.right.item == item:
                # 返回某点，就是寻找的父结点
                return pop_node
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)

    def delete(self, item):
        if self.root is None:
            return False
        parent = self.get_parent(item)
        if parent:
            del_node = parent.left if parent.left.item == item else parent.right
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
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
                    # 将tmp指向右子树的最后一个结点
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
            return False



t = Tree()
t.add(1)
t.add(2)
t.add(3)
t.add(4)
print(t.get_parent(3))
t.delete(1)
print(t.get_parent(4))
print(t.get_parent(3))



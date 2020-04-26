class Node(object):
    def_init_ (self, item):
       self .item = item
       self .left = None
       self .right = None
    def_str_ (self):
       return str(self. item) # print 一个node类时会打印——str——的返回值


class Tree(object):
    def_ init_ (self):
       self.root = Node("root") #根节点定义为root永不删除
    def add(self,item):
        node = node(item):
        if self.root is none: #如果二叉树为空，那么生成的二叉树最终为新插入
            self.root = node
        else:
            q = [self.root]#将q列表添加二叉树的根节点
            while True:
                pop_node = q.pop(0)
                if pop_node.left = is None:##如果左子树为空，则将该点添加到左子树
                    pop. node.left = node
                    return
                elif pop_ node.right is None: #右子树为空则将点添加到右子数
                    pop_ node.right = node 
                    return
                else:
                    q. append(pop_ node . left)
                    q. append(pop node)

    def insertLeft(self, item): 
node
= Node(item)
        if self.root.left is None:
            self .root.1eft = node
        else :
            node.left = self. root. left
            self .root.left = node
    def insertRight(self, item):
            node = Node( item)
        if self .root.right is None:
            self .root. right = ncHe
        else :
            node .right = self . root .right
            self . root.right = node
    def get_ parent(self, item):
        if self.root. item == item:
            return None #根节点没有父节点
        tmp = [self . root]
        while tmp:
            pop_ node = tmp . pop(0)|
        #某一点的右子树为寻找的点
        if pop_ node.left and pop_ node.left. item == item:
           return pop_ node#返回某点，就是寻找的父节点
        if pop_ node.left is not None:
            tmp . append(pop_ node . left)
        if pop_ node.right is not None : 
            tmp. append(pop_ node . right)
    def delete(self, item) :
        if self.root is None :
           return False
        parent = self. get_ parent( item)
        if parent:
           del_node = print.left if print.left.item == item else parent. right
        if del node.1eft is None:
            if print. left.item == item:
              parent.left = del_ node . right
            else:
                parent.right = del_ node . right
            del del_ node
            return True
        elif del node .right is None:
            if parent.left.item == item:
                parent.left = del_ node.left
            else :
                parent.right = del_ node .1eft
        del del_ node
            return True
        else:
            while tmp_ next. left: #将tmp指向右了树的最后一个 节点
                tmp_ pre = tmp_ next
                tmp_ next = tmp_ _next.left
            tmp_ pre.left = tmp next. right
            tmp_ next.left = del node.1eft
            tmp_ next.right = del node. right
        if parent.1eft. item == item:
            parent. left = tmp next
        else:
            parent.right = tmp_ next
        del del node
        return True
    return False






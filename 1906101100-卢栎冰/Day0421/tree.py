class Node(object):
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
    def __str__(self):
        return str__(self.item)#print一个Node类时会打印__str__返回

class Tree(object):
    def __init__(self):
        self.root=Node('root')#根节点定义为root，永不删除
    def add(self,item):
        node=Node(item)
        if self.root is None :#如果问茶树为空，那吗生成的二叉树最终为新插入
            self.root=node
        else:
            q=[self.root]#将q列表添加二叉树的根节点
            while True:
                pop_node=q.pop(0)
                if pop_node.left is None:
                    pop_node.left=node
                    return
                elif pop_node.right is None:
                    pop_node.right=node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    
       
    def insertLeft(self,item):
        node=Node(item)
        if self.root.left is None:
            self.root.left=node
        else:
            node.left=self.root.left
            self.root.left=node
    def insertRight(self,item):
        node=Node(item)
        if self.root.right is None:
            self.root.right=node
        else:
            node.right=self.root.right
            self.root.right=node
    def get_parent (self, item):
        if self.root. item == item:
            return None #根节点没有父节点
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)#某一点的左子树为寻找的点
            if pop_node.left and pop_node.left.item==item:
                return pop_node #返回某点，就是寻找的父节点
                #某点的右子树为寻找的点
            if pop_node.right and pop_node.right.item==item: 
                return pop_node#返回某点，就是寻找的父节点
            if pop_node.left is not None:
                tmp.append(pop_node.left )
            if pop_node.right is not None: 
                tmp.append(pop_node.right)

    def delete (self,item):                                                                                 
        if self.root is None:
            return False
        parent=self.get_parent(item)
        if parent:
            del_node=parent.left if parent.left.item == item else parent.rightf 
            if del_node.left is None:
                if parent.left.item==item:
                    parent.left=del_node.right
                else:
                    parent.right=del_node.left
                del del_node
                return True
            elif del_node.right.iten==item:
                if parent.left.iten==item:
                    parent.left=del_node.1eft
                else:
                    parent.right=del_node.left
                del del_node
                return True
            else:#左右子树都不为空
                tmp_pre=del_node
                tmp_next=del_node.right
                if tmp_next.left is None:
                    tmp_pre.right=tmp_next.right
                    tmp_next.left=del_node.left
                    tmp_next.right=del_node.right
                else:
                    while tmp_next.left:#将tmp指向右子树的最后一个节点
                        tmp_pre=tmp_next
                        tmp_next=tmp_next.left
                    tmp_pre.left=tmp_next.right
                    tmp_next.left=del_node.left
                    tmp_next.right=del_node.right
                if parent.left.item==item:
                    parent.left=tmp_next
                else:
                    parent.right=tmp_next
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



#遍历
#前序，中序，后序pre order,middle oreder ,post order
ls=[]
#前序遍历
def pre(root,ls):
    #如果节点为空(如果为叶子节点)
    if not root:
        return 
    #前序
    ls.append(root.val)#根 
    pre(root.left,ls)#左
    pre(root.right,ls)#右
#中序遍历
def mid(root,ls):
    #如果节点为空(如果为叶子节点)
    if not root:
        return
    #中序
    mid(root.left,ls)#左
    ls.append(root.val)#根
    mid(root.right,ls)#右
#后序
def post(root,ls):
    #如果节点为空(如果为叶子节点)
    if not root:
        return
    #后序
    post(root.left,ls)#左
    post(root.right,ls)#右
    ls.append(root.val)#根




    





                      
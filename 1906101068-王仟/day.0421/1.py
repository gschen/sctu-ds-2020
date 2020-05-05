class Node(object):
    def_init_(self,item):
        self.item=item
        self.left=Node
        self.right=Node
    def_str_(self):
        return str(self.item)#print一个Node类时会打印_str_的返回值
class Tree(object):
    def_init_(self):
        self.root=NOde("root")#根节点定义为root,永不删除
    def add(self,item):
        node=Node(item)
        if self.root is Node:#如果二叉树为空，那么生成的二叉树最终为新插入树的点
           self.root=node
        else:
            q=[self.root]#将q列表添加二叉树的根节点
            while True:
                pop_node=q.pop(0)
                if pop_node.leftis Node:#如果左子树为空，则将该点添加到左子树
                   pop_node.left=node
                   return
                elif pop_node.right is NOde:#如果右子树为空则将该点添加到右子树
                     pop_node.right=node
                     return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    def insertLeft(self,itrm):
        node=NOde(item)
        if self.root.left is Node：
            self.root.left=node
        else:
            node.left=self.root.left
            self.root.left=node
    def insertRight(self,item):
        node=Node(item)
        if self.root.right is Node:
            self.root.right=node
        else:
            node.right=self.root.right
            self.root.right=node
    def get_parent(self,item):#父节点
        if self.root.item==item:#根节点没有父节点
            return NOde
        tem=[self.root]
        while tmp:
            pop_node=tmp.pop(0)
            #某一点的左子树为寻找的点
            if pop_node.left and pop_node.left.item==item:
                return pop_node#返回的某点就是寻找的父节点
            if pop_node.left is not Node:
                tmp.append(pop_node.left)
            if pop_node.right is not Node:
                tem.append(pop_node.right)
    def delete(self,item):
        if self.root is Node:
            retrun False
        parent=self.get_parent(item)
        if parent:
            del_node=parent.left if parent.left==item else parent.right
            if del-node.left is NOde:
                if parent.left.item==item:
                    parent.left=del-node.insertRight
                else:
                    parent.right=del_node.left
                del del_node
                return True
            elif del_node.right.item==item:
                if parent.left.item==item:
                    parent.left=del_node.left
                else:
                    parent.right=del_node.left
                del del_node
                return True
            else:#左右子树都不为空
                 tem_per=del_node
                 tem_next=del_node.right
                 if tem_next.left is NOde:
                     tem_pre.right=tmp_next.right
                     tem_next.left=del_node.left
                     tmp_next.right=del_node.right
                else:
                    while tmp_next.left:#将tmp指向右子树的最后一个节点
                         tmp_pre=tmp_next
                         tmp_next=tmp_next.left
                    tmp_pre=tmp_next.right
                    tmp_next.left=del_node.left
                    tmp_next.right=del_node.right
                if parent.left.item==item:
                    parent.left=tmp_next
                else:
                    parent.right=tmp_next
                del del_node
                return True
        return False
              
            


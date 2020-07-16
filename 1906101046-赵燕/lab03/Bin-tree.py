#定义节点类
class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


class Bintree:

    def __init__(self,root):
        self.root = root


    def is_empty(self):#判断是否为空


        if self.root is None:
            return True

        else:
            return False

    #先序遍历
    def preorder(self,root):

        if root is None:
            return 
        print(root.data,end=' ')
        self.preorder(root.left)
        
        self.preorder(root.right)

    #中序遍历
    def midorder(self,root):

        if root is None:
            return
        
        self.midorder(root.left)

        print(root.data,end=' ')

        self.midorder(root.right)

    #后序遍历
    def postorder(self,root):

        if root is None:
            return
        
        self.midorder(root.left)

        self.midorder(root.right)

        print(root.data,end=' ')




# ls=[]
# def pre(root):#前序
#     if not root:
#         return
#     ls.append(root.val)
#     pre(root.left,ls)
#     pre(root.right,ls)
# def mid(root,ls):
#     if not root:
#         return
#     mid(root.left,ls)
#     ls.append(root.val)
#     mid(root.right,ls)
# def back(root,ls):
#     if not root:
#         return
#     back(root.left,ls)
    
#     back(root.right,ls)
#     ls.append(root.val)




if __name__ == "__main__":
    
    h = Node('H')

    g = Node('G')

    i = Node('I')

    j = Node('J')

    k = Node('K')

    d = Node('D',None,h)

    
    e = Node('E',None,i)

    b = Node('B',d,e)

    f = Node('F',j,k)

    c = Node('C',f,g)

    a = Node('A',b,c)

    bt = Bintree(a)
    bt.preorder(bt.root)
    print()
    bt.midorder(bt.root)
    print()
    bt.postorder(bt.root)

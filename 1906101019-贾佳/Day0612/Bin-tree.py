class Node:

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right



class Bintree:
    def __init__(self,root):
        self.root = root
    
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
#先序遍历
    def preorder(self,root):
        if root is None:
            return
        print(root.data,end = " ")
        self.preorder(root.left)
        self.preorder(root.right)

#中序遍历
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
#后序遍历
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")


if __name__ == "__main__":
    g = Node("G")
    h = Node("H")
    i = Node("I")
    j = Node("J")
    k = Node("K")
    d = Node("D",None,h)
    e = Node("E",None,i)
    b = Node("B",d,e)
    f = Node("F",j,k)
    c = Node("C",f,g)
    a = Node("A",b,c)
    print("前序遍历")
    bt = Bintree(a)
    bt.preorder(bt.root)
    print("\n")
    print("中序遍历")
    bt.inorder(bt.root)
    print("\n")
    print("后序遍历")
    bt.postorder(bt.root)
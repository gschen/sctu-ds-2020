class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def getllElements(slef,root1:TreeNode,root2:TreeNode) :
    l=[]
    def f(root):
        if root:
            l.append(root.val)
            f(root.right)
            f(root.left)
    f(root1)
    f(root2)
    l.sort()
    return l
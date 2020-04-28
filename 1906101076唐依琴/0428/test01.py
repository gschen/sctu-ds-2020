#Definition for a binary tree node.
#class TreeNode:
#    def __init__(self,x):
#        self.val=x
#        self.left=None
#        self.right=None
class Soulution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        L=[]
        def t(root):
            if root:
                L,append(root,val)
                t(root.right)
                t(root.left)
        t(root1)
        t(root2)
        L.sort()
        return L

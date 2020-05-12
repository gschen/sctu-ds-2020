#Definition for a binary tree Node.
#class TreeNode:
#    def __init__(self,x):
#        self.val=x
#        self.left=None
#        self.right=None


ls=[]
def pre(root,ls):
    if not root:
        return

ls.append(root.val)
pre(root.left,ls)
pre(root.right,ls)


ls=[]
class Solution:
    def getAllElements(self,root1:TreeNode,root2:TreeNode):
        ls=[]
        def f(root):
            if root:
                if root:
                    ls.append(root.val)
                    f(root.right)
                    f(root.left)
        f(root1)
        f(root2)
        ls.sort()
        return ls

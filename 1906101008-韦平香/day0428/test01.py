#def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#Definition for a binary tree node:
#    class TreeNode:
#        def __init__(self,x):
#            self.val=x
#            self.left=None
#            self.right=None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
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

def isSymmetric(self,root:TreeNode) -> bool:
    if not root:
        return True

    def dfs(root):
        if root.left.value!=root.right.value:
            return False
        if not root.left or not root.right:
            return False
        if not root.left and not root.right:
            return True

         return dfs(root.left,root.right)
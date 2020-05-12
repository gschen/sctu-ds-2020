# class TreeNode:
#     def __init__(self,x):
#         self.val=x
#         self.left=None
#         self.right=None

class Solution:
def getElements(self,root1:TreeNode,root2:TreeNode) ->List[int]:
    ls=[]
    def f(root):
        if root:
            ls.append(root.val)
            f(root.right)
            f(root.left)
        f(root1)
        f(root2)
        ls.sort()
        return 1
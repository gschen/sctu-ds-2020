# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l=[]
        def pre(root,l):
            if not root:
                return
            l.append(root.val)
            pre(root.left,l)
            pre(root.right,l)
        pre(root1,l)
        pre(root2,l)
        l.sort()
        return l

    

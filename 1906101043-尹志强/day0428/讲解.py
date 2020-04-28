# Definition for a binary tree node
# class TreeNode:
#    def__init__(self,x):
#        self.val=x
#        self.left=None
#        self.right=None

# class Solution:
#     def getllElements(slef,root:TreeNode,root2:TreeNode) -> List[int]:
#         l=[]
#         def f(root):
#             if root:
#                 l.append(root.val)
#                 f(root.right)
#                 f(root.left)
#         f(root1)
#         f(root2)
#         l.sort()
#         return l
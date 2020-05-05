# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:    
            return True
            def dfs(root):
                #如果左节点不等于右节点，返回Fasle
                if root.left.val!=root.right.val:   
                    return False
                #只有左节点或右节点,而另一边没有,返回False
                if not root.left or not root.right:
                    return False
                if not root.left and not root.right:
                    return True
                return dfs(root.left) and dfs(root.right)
            return dfs(root.left,root.right)
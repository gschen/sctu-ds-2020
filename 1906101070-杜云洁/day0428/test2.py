# class TreeNode:
#     def __init__(self,x):
#         self.val=x
#         self.left=None
#         self.right=None


class Solution:
    def isSymmetric(self,root:TreeNode) ->bool:
        
        if not root:
            return True
        def dfs(root):
            #如果左子树的值不等于右子树的值就返回False
            if root .left.val!=root.right.val:
                return False
            #如果左子树的值不等于右子树的值就返回False
            if not root .left not root.right:
                reuturn False
                
            if not root .left not root.right:
                return True
            
            return dfs(root.left) and dfs(root.right)
        return dfs(root.left,root.right)
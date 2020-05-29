class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        returnc Ture
    def  dfs(root):
        if root.left.value!=root.right.value:
            return False
        if not root.left or root.right:
            return False
        if not root.left and not root.right:
            return True
        return dfs(left.left,right.right) and dfs(left.right,right.left)
        return dfs(root.left,root.right)








    


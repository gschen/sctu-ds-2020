def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True

    def dfs(root):
        if root.left.value != root.right.value:
            return False
        if not root.lefft or not root,right:
            return False
        if not root.left and not root.right:
            return True

        return dfs(root.left) and dfs(root.right)



class Solution:
    def isSymmetric(self,root:TreeNode) -> bool:
        if not root:
            return True
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return dfs(left.left,right.right) and dfs (left.right,right.left)
        return dfs(root.left,root.right)
                
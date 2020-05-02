def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True
    def dfs(root):
        if root.left.value!=root.right.value:
            return False
        if not root.left or not root.right:
            return False
        if not root.left and not root.right:
            return True
        return dfs(root.left) and dfs(root.right)
    return dfs(root.left,root.right)
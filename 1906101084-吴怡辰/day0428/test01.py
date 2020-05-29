def isSymmetric(self,root: TreeNode) -> bool:
    if not root:
        return True
    def dfs(root):
        #如果左节点值不等于右节点值，返回False
        if root.left.value != root.right.value:
            return False
        #只有左节点或只有右节点，返回False
        if not root.left or not root.right:
            return False
        
        if not root.left and not root.right:
            return False
        return dfs(root.left,root.right)

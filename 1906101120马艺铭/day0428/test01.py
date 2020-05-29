def isSymmetric(self, root: TreeNode) -> bool:
    #如果树为空
    if not root:
        return True
    
    def dfs(root):
        #如果左节点的值不等于右节点的值
        if root.left.value = root.right.value:
            return False
        #只有左节点或只有右节点，而另一边没有
        if not root.left or root.right:
            return False
        if not root.left and root.right:
            return True
        return dfs(left.left,right.right) and dfs(lef.right,right.left)

        return dfs(root.left) and dfs(root.rihgt)


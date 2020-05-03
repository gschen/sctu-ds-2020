def isSymmetric(self,root:TreeNode)->bool:
    #如果树为空
    if not root:
        return True
    def dfs(root):
        #如果左节点的值不等于右节点的值
        if root.left.value!=root.right.value:
            return False
        #只有左节点或者只有右节点
        if not root.left or not root.right:
            return False
        if not root.left and not root.right:
            return True

        return dfs(root.left) and dfs(root.right)
def isSymmetric(self, root: TreeNode) -> bool:
    #如果树为空
    if not root:
        return True
    def dfs(root):
        #判断左右节点是否相等
        if root.left.value !=root.right.value:  
            return False
        #只有左节点或者右节点，则返回FALSE
        if not root.left or not root.right:
            return False
        if not root.left and not root.right:
            return True
        return dfs(root.left) and dfs(root.right)
    return dfs(root.left) and dfs(root.right)

           


        

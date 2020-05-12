class Solution: 
    def isSymmetric(self, root):
    # 如果为空
        if not root:
            return True

        def dfs(root):
        # 如果左节点不等于右节点的值。返回False
            if root.left.value!=root.right.value:
                return False
        # 只有做节点或者只有右节点，而另一边没有，返回false
            if not root.left or not root.right:
                return False
            if not root.left and not root.right:
                return True
        return dfs(root.left) and dfs(root.right)
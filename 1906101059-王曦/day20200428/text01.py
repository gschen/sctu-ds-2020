class Solution:
    def getllElements(slef,root1:TreeNode,root2:TreeNode) -> List[int]:
        l=[]
        def f(root):
            if root:
                l.append(root.val)
                f(root.right)
                f(root.left)
        f(root1)
        f(root2)
        l.sort()
        return l


def isSymmetric(self, root: TreeNode) -> bool:
    # 如果树为空
    if not root:
        return True

    def dfs(root):
        # 如果左节点的值不等于右节点的值，返回False
        if root.left.value != root.right.value:
            return False
        # 只有左节点或者只有右节点，而另一边没有，则返回False
        if not root.left or not root.right:
            return False

        if not root.left and not root.right:
            return True

        dfs(root.left) and dfs(root.right)
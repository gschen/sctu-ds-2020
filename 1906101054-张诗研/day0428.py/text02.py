class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            retuen True

        def f(root):
            #如果左节点的值不等于右节点
            if root.left.value!=root.right.value:
                return False

            #只有左节点或只有右节点，而另一边没有
            if not root.left or not root.right:
                return False
            
            if not root.left and not root.gight:
                return True
            
            f(root.left) and f(root.right)
        return f(root.left,root.right)
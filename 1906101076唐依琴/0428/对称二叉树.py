class Soulution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #如果树为空
        if not root:
            return True
    
    def tyq(root):
        #如果左节点的值不等于右节点的值，返回False
        if root.left.value!=root.right.value:
            return False
        #只有左节点或者只有右节点，而另一边没有，返回False
        if not root.left or root.right:
            return False
        
        if not root.left and not root.right:
            return True
        
        return tyq(root.left) and tyq(root.right)
    return tyq(root.left,root.right)


ls = []
        def pre(root):
            if root:
                ls.append(root.val)
                pre(root.left)
                pre(root.right)
        pre(root1)
        pre(root2)
        ls.sort()
        return ls



def isSymmetric(self, root: TreeNode) -> bool:
    #如果树为空
    if not root:
        return True

    def dfs(root):
        #如果左节点的值不等于右节点的值，返回False
        if root.left.value!=root.right.value:
            return False
        #只有左节点或者只有右节点，而另一边没有，则返回False
        if not root.left or not root.right:
            return False

        if not root.left and not root.right:
            return True
        
        defs(root,left) and dfs(root.right)


#Definition for a binary tree node
#class TreeNode:
#    def__init__(self,x):
#        self.val=x
#        self.left=None
#        self.right=None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    #如果树为空
    if not root:
        return True
    def dfs(left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        #如果左节点的值不等于右节点的值，返回False
        if left.val!=right.val:
            return False
        return dfs(left.left,right.right) and dfs(left.right,right.left)
    return dfs(root.left,root.right)        
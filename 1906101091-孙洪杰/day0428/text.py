
class Solution:
    def getAllElements(self,root1:TreeNode,root2:TreeNode)->List[int]:
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

Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        L = []
        def ycx(root):
            if root == None:
                return
            L.append(root.val)
            ycx(root.left)
            ycx(root.right)
        ycx(root1)
        ycx(root2)
        return list(sorted(L))

#对称二叉树
Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
#方法一
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        l1=[]
        l2=[]
        def bl1(root):
            if root:
                l1.append(root.val)
                bl1(root.right)
                bl1(root.left)
            l1.append(0)
        def bl2(root):
            if root:
                l2.append(root.val)
                bl2(root.left)
                bl2(root.right)
            l2.append(0)
        bl1(root.right)
        bl2(root.left)
        if l1==l2:
            return True
        else:
            return False

#方法二
class Solution:
    def isSymmertric(self,root:TreeNode) -> bool:
        #如果树为空，则对称
        if not root:            
            return True
        
        def yc(root):
                if root.left.value!=root.right.value:
                return False#如果左节点的值不等于右节点的值，则不对称
            if not root.left or not root.right:
                return False#只有左节点或者只有右节点而另一边没有，则不对称
            if not root.left and not root.right:
                return True
            
            return yc(root.left) and yc(root.right)
        return yc(root.right,root.left)





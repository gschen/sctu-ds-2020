#Definition for a binary tree node.
class TreeNode:
   def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None
class Soulution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        L=[]
        def D(root):
            if root:
                L.append(root.val)
                D(root.right)
                D(root.left)
        D(root1)
        D(root2)
        L.sort()
        return L

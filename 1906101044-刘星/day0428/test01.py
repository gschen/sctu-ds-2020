l=[]
def PreOrder(root):
    if not root:
        return
    l.append(root.val)
    PreOrder(root.left)
    PreOrder(root.right)

class Solution:
    def getAllElements(self,root1:TreeNode,root2:TreeNode)->List[int]:
        PreOrder(root1)
        PreOrder(root2)
        l.sort()
        return l
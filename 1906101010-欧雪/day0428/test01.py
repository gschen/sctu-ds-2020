L=[]
def pre(root):
    global L
    if root==None:
        return 
    L.append(root.val)
    pre(root.left)
    pre(root.right)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        pre(root1)
        pre(root2)
        return list(sorted(L))
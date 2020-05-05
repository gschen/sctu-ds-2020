ls=[]
def pre(root):
    if not root:
        return
    ls.append(root.val)
    pre(root.left)
    pre(root.right)


class Soultion:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
       pre(root1)
       pre(root2)
       ls.sort()
       return ls
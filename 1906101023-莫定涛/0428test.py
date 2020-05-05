def pre(root,ls):
    if not root:
        return

    ls.append(root.val)
    pre(root.left,ls)



def PreOrder(root):
    global L
    if root == None:
        return
    L.append(root.val)
    PreOrder(root.left)
    PreOrder(root.right)

class Solution:
    def getAllElements(self,root1:TreeNode,root2:TreeNode) -> List[int]:
        PreOrder(root1)
        PreOrder(root2)
        return list(sorted(L))




        
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l=[]
        def pre(root):
            if root:
                l.append(root.val)
                pre(root.right)
                pre(root.left)
        PreOrder(root1)
        PreOrder(rooy2)
        return list(sorted())
    
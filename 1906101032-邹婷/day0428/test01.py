class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l=[]
        def p(root):
            if root:
                l.append(root.val)
                p(root.left)
                p(root.right)
        p(root1)
        p(root2)
        l.sort()
        return l
class Solution:
    def getAllElements(self,root1:TreeNode,root2:TreeNode) -> List[int]:
        L=[]
        def t(root):
            if root:
                L.append(root,val)
                t(root.right)
                t(root.left)
        t(root1)
        t(root2)
        L.sort()
        return L
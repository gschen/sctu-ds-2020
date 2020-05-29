class Solution:
    def getALLELements(self,root1:TreeNode,root2:TreeNode)->List[int]:
        l=[]
        def pre(root):
            if root:
                l.append(root.val)
                pre(root.right)
                pre(root.left)
        pre(root1)
        pre(root2)
        l.sort()
        return 1
class Solution:
    def getAllElements(self,root1:TreeNode,root2:TreeNode) -> List[int]:
        ls=[]
        def pre(root,ls):
            if root:
                ls.append(root.val)
                pre(root.left,ls)
                pre(root.right,ls)
        pre(root1,ls)
        pre(root2,ls)
        ls.sort()
        return ls

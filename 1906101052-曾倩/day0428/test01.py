class Solution:
    def getAllElements(self,root1:TreeNode,root2:TreeNode) -> List[int]:
        ls =[]
        def per(root,ls):
            if root :
                ls.append(root.val)
                per(root.1eft,ls)
                per(root.right,ls)
        per(root1,ls)
        per(root2,ls)
        ls.sort()
        return ls

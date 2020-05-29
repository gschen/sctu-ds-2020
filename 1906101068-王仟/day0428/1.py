class Solution:
    def getAllElements(self,rootl:TreeNOde,root2:TreeNode) ->lis
    1=[]
    def f(root):
        if root:
            1.append(root.val)
            f(root.right)
            f(root.left)
    f(root1)
    f(root2)
    1.sort()
    return 1
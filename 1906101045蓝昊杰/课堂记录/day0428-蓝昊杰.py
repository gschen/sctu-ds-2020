# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         L=[]
#         def ycx(root):
#             if root == None:
#                 return
#             L.append(root.val)
#             ycx(root.left)
#             ycx(root.right)
#         ycx(root1)
#         ycx(root2)
#         return list(sorted(L))



def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True
    def dfs(root):
        #如果左节点的值不等于右节点的值，返回Flase
        if root.left.value!=root.right.value:
            return False
        #只有左或右节点，返回False
        if not root.left or not root.right:
            return False
        if not root.left and not root.right:
            return True
        return dfs(root.left.left,root.right.right) and dfs(root.left.right,root.right.left)
    return dfs(root.left) and dfs(root.right)
class Solution:   
    def isSymmetric(self, root: TreeNode) -> bool:
        #如果树为空
        if not root:
            return True

        def dfs(root):
            #如果左节点的值不等于右节点的值，返回False
            if root.left.value!=root.right.value:
                return False
            #只有左节点或者只有右节点，而另一边没有，返回False
            if not root.left or not root.right:
                return False

            if not root.left and not root.right:
                return True

            return dfs(root.left) and dfs(root.right)



# class Solution:   
#     def isSymmetric(self, root: TreeNode) -> bool:
#         #如果树为空
#         if not root:
#             return True
#         def dfs(left,right):
#             if not left and not right:
#                 return True
#             if not left or not right:
#                 return False
#             if left.val!=right.val:
#                 return False
#             return dfs(left.left,right.right) and dfs(left.right,right.left)
#         return dfs(root.left,root.right)
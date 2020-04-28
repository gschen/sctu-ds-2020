# coding=utf-8

'''
1305. 两棵二叉搜索树中的所有元素

给你 root1 和 root2 这两棵二叉搜索树。
请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

示例 1：
输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]

示例 2：
输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
输出：[-10,0,0,1,2,5,7,10]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l=[]
        def f(root):
            if root:
                l.append(root.val)
                f(root.right)
                f(root.left)
        f(root1)
        f(root2)
        l.sort()
        return l


#----------------------------------------------------------------------------


'''
101. 对称二叉树

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
'''
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        l1,l2=[],[]
        right=root.right
        left=root.left
        def r(root):
            if root:
                l1.append(root.val)
                r(root.right)
                r(root.left)
            l1.append('None')
        def l(root):
            if root:
                l2.append(root.val)
                l(root.left)
                l(root.right)
            l2.append('None')
        r(right)
        l(left)
        return l1==l2
'''
# 学长的解法
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 如果树为空
        if not root:
            return True
        def dfs(left,right):
            # 左节点值不等于右结点值，返回Flase
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        return dfs(root.left,root.right)
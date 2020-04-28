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

def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True
    def d(root):
        if root.left.value!=root.right.value:
            return False
        if not root.left or not root.right:
            return False#只有做节点或者只有右节点 而列一边没有 返回false
        if not root.left and not root.right:
            return True

        return d(root.left) and d(root.right)   
                


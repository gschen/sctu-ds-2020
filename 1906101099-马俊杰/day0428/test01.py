'''
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l=[]
        def f(foot):
            if root:
                l.append(root.val)
                f(root.right)
                f(root.left)
        f(root1)            
        f(root2)
        l.sort()
        return l
'''        
'''
def isSymmetric(self, root: TreeNode) -> bool:
#如果树为空
    if not root:
        return True

def des(root):
#如果左节点的值不等于右节点的值，返回False
    if root.left.value != root.right.value:
        return False
#如果只有左节点或只有右节点，而另一边没有，返回False        
    if not root.left or not root.right:    
        return False
    if not root.left or not root.right:
        return True

    return dfs(root.left) and dfs(root.right)
return dfs(root.left,root.right)    
'''
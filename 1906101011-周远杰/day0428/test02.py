def isSymmetric(self,root): 
    #如果树为空
    if not root:
        return True
    
    def dfs(root):
        #如果左结点的值不等于右结点的值，返回Flase
        if root.left.value!=root.value:
            return False
        #只有左结点或者只有右结点，而另一边没有，返回False
        if not root.left or not root.right:
            return False
        #左右结点都没有
        if not root.lrft and not root.right:
            return True
        return dfs(left.left,right.right) and dfs(left.right,right.left)
    return dfs(root.left) and dfs(root.right)

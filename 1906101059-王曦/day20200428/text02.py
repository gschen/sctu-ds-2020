class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #如果树为空
        if not root:
            return True
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            #如果左节点的值不等于右节点的值，返回False
            if left.val!=right.val:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        return dfs(root.left,root.right)

class Solution:
    def mergeKLists(self,lists: ListNode) -> ListNode:
        if lists==[]:
            return lists
        l=[]
        for i in lists:
            while i:
                l.append(i.val)
                i=i.next
        l.sort()
        if l==[]:
            return lists
        a = b= ListNode(l[0])
        for j in l[1:]:
            b.next=ListNode(j)
            b=b.next
        return a
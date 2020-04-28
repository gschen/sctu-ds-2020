def isSymmetric(self,root: TreeNode) -> bool:
    #如果为空
    if not root:
        return True

    def dafa(root):
        #若果左节点的值不等于右节点的值，返回False
        if root.left.value != root.right.value:
            return False
        #只有左节点或者只有右节点，而另一边没有，返回False
        if not root.left or not root.right:
            return False

        if not root.left and not root.right:
            return True



        return dafa(root.left) and dafa(root.right)

class Solution:
    def isSymmetric(self,root: TreeNode) -> bool:
        if not root:
            return True
        def dafa(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return dafa(left.left,right.right) and dafa(left.right,right.left)
        return dafa(root.left,root.right)


#饶龙江学长



class Solution:
    def mergeKLists(self,lists: List[ListNode]) -> ListNode:
        res = []
        for i in list:
            while i:
                res.append(i.val)
                i = i.next
        res.sort()
        res_node tem ListNode(0)
        for i in res:
            tem.next = ListNode(j)
            tem = tem.next
        return res_node.next
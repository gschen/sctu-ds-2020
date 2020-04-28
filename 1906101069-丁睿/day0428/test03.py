#对称二叉树
def isSymmetric(self,root:TreeNode)-> bool:
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
                l1.append("None")
        def l(root):
            if root:
                l2.append(root.val)
                l(root.left)
                l(root.right)
            l2.append("None")
        r(right)
        l(left)
        return l1==l2


        
#合并k个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
class Solution:
    def mergeKLissts(self,lists:List[ListNode])->Listnode:
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
        a=b=ListNode(l[0])
        for j in l[1:]:
            b.next=ListNode(j)
            b=b.next
        return a
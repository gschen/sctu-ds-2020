class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_list, l2_list = [], []
        l1_list_num, l2_list_num= 0, 0
        head = ListNode(0)
        node = head

        while l1 != None:            #链表转list
            l1_list.append(l1.val)
            l1 = l1.next
        while l2 != None:            
            l2_list.append(l2.val)
            l2 = l2.next

        for i in range(len(l1_list)):    #计算对应数值
            l1_list_num += l1_list[i] * 10**i
        for i in range(len(l2_list)):
            l2_list_num += l2_list[i] * 10**i
        ans = l1_list_num + l2_list_num
        
        if ans == 0:
            node.next = ListNode(0)
        while ans != 0:               
            ansmod = ans % 10
            node.next = ListNode(ansmod)
            ans = ans / 10
            node = node.next
        return head.next


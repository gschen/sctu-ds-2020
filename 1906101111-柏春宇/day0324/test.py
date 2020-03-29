class Find:
    def middleNode(self, head):
        cur=cur=head
        while cur and cur.next:
            if cur.next.next==None:
                return cur.next
            cur=cur.next
            cur=cur.next.next
        return cur
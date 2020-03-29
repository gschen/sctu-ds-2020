class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next
class Solution:
    def MiddleNode(self,head):
        if head is None:
            return None
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.value
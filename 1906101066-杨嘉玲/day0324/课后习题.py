class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class SingleLink():
    def __init__(self,node=None):
        self.__head=node
    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def new_link(self):
        if count/2 != 0:
            cur = self.__head
            for i in ((count+1)/2+1):
                cur = cur.next
            node.next = cur
        else:
            for i in (count/2+1):
                cur = cur.next
            node.next = cur

            
                



            

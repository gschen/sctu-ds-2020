class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def length(self):
        
        cur=self.__head
        count=0 
        while cur!=None:
            
            count+=1

            
            cur=cur.next
        return count

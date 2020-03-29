class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Signallink():
    def __init__(self,node=None):
        self.__head=node

    def length(self):
        
        cur=self.__head
        count=0 
        while cur!=None:
            
            count+=1

            
            cur=cur.next
        return count
s1=Signallink(1)
print(s1.length())
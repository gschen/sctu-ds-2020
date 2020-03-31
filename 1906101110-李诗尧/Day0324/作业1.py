class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SigleLink():
    def __init__(self):
        self.head=Node(-1)
    def travel(self,value):
        cur=self.head
        ans=[]
        count=0
        while cur!=None:
            cur=cur.next
            ans.append(cur)
            count+=1
        s=count//2
        if count%2==1:
            ans=ans[s::]
        else:
            ans=ans[s+1::]
        return ans
sl=SigleLink() 

print(sl.travel(6))
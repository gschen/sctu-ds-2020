class Soultion:
    def mergKLists(celf,lists:List[listNode]) - >ListNode:
        if list==[]:
            return lists
    l =[]
    for i in lists:
        while i :
            l.append(i.val)
            i=i.next
    l.sort()
    if l==[]:
        return lists
    a=b=ListNode(j)
    for j in l[i:]:
        b.next=listNode(j)
        b=b.next
    return a
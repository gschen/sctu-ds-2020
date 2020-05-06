class ListNode():#定义一个节点类
    def __init__(self,data):
        self.val = data
        self.next = None
def mergeKlists(lists):
    ls = []  #定义一个列表存入所有链表的值
    for i in lists: #遍历所有链表，i代表每个链表的头节点
        while i != None:
            ls.append(i.val)
            i = i.next
    ls.sort() #将所有链表的值进行排序
    if ls == []: #如果链表为空，则返回空列表
        return ls
    res = ListNode(ls[0])#将列表第一个值赋给res，作为头节点值
    p = res #又将res赋值给p，作为尾插法的尾结点
    for o in ls[1:]:#遍历出首元素外列表所有元素
        p.next = ListNode(o)#将其转化为节点对象
        p = p.next#让p等于当前链表的尾结点
    return res#最后返回所得链表的头节点
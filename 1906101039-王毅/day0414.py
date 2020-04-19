n=eval(input())
def fib(a=1,b=1,k=2):
    if k==2:
        return b
    return fib(b,a+b,k+1)

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None

class SingleLink():
    def __init__(self):
        self._head=None
    def add_tail(self,val):
        node=Node(val)

        if self._head==None:
            self._head=node
        else:
            cure=self._head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

def travel(self):
    cur=self._head
    while ur.next!=None:
        print(cur.val)
        cur=cur.next

def f_tra(self):
    def tra(node):
        if node==None:
            return
        print(node.val)
        tra(node.next)
    tra(self._head)

a=SingleLink()
a.add_tail(10)
a.add_tail(20)
a.add_tail(30)
#a.travel()
a.f_tra()


#机算回退下标
def back_index(s):
    lis=[-1]#代表第一个字符
    k=-1#最长公共前缀
    for i in range(1,len(s)):
        if s[i]==s[k+1]:#满足情况，最长公共前缀加一
            k=k+1
        while s[i]!=s[k+1] and k>-1 :#不满足情况，需要不断往回退，同时避免退回到-1
            k=lis[k]
        if s[i]==s[k+1]:
            k=k+1#满足情况，最长公共前缀加一
        lis.append(k)
    return lis
print(back_index('aba'))


def kmp(s1,s2): #s1是母串，s2是子串
    s2_lis=back_index(s2)
    k=-1#代表的是相同的序列长度
    for i in range(len(s1)):
        #需要回退的情况
        while k>-1 and s1[i]!=s2[k+1]:
            k=s2_lis[k]
        #相同序列
        if s1[i]==s2[k+1]:
            k=k+1
        #当k=len(s2)-1
        if k==len(s2)-1:
            lis.append(i)
            k=s2_lis[k]
    return lis
            
print(kmp())
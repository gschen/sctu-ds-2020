#斐波拉契数列
n=eval(input())
def fib(a=1,b=21,k=2):
    if k==n:
        return b
    return fib(b,a+b,k+1)
print(fib())

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))


class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SingleLink():
    def __init__(self):
        self._head = None

    def add_tail(self, val):
        node = Node(val)

        if self._head == None:
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.val)
            cur = cur

    def f_tra(self):

        def tra(node):
            if node == None:
                return
            tra(node.next)
            print(node.val)

        tra(self._head)


a = SingleLink()
a.add_tail(10)
a.add_tail(20)


#计算回退下标
def back_index(s):
    lis=[-1]#表示第一个字符
    k=-1#最长公共前缀
    for i in range(1,len(s)):
        while s[i]==s[k+1]:#满足情况，最长公共前缀+1
            k=k+1
        if s[i]==s[k+1] and k>-1:#不满足情况，需要不断回退，同时避免回退到-1
            k=lis[k]
        lis.append(k)
    return lis
print(back_index('ababaca'))
def kmp(s1,s2):#s1是母串,s2是子串
    s2_lis=back_index(s2)
    k=-1#代表的是相同的序列长度
    lis=[]
    for i in range(len(s1)):
        #需要回退的情况
        while k>-1 and s1[i]!=s2[k+1]:
            k=s2_lis[k]
        #相同序列
        if s1[i]==s2[k+1]:
            k=k+1
        #当k=len(s2-1时，代表匹配成功
        if k==len(s2)-1:
            lis.append(i)
            k=s2_lis[k]#每次匹配后，需要回退，不然后续会超出
    return lis

print(kmp('abaabcab','abc'))
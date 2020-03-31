 a = LinkNode()
l = list(map(int,input().split()))
a.insert_tail(l)
p = a.head
res = []
count = 0
while p.next != None:
    p = p.next
    res.append(p.value)
    count += 1
print(res[count//2:])
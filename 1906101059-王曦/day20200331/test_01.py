l = list(input().split())
stack = []
for i in l :
    if i!='c' and i!='d' and i!='+':
        stack.append(int(i))
    if i == 'c':
        stack.pop(-1)
    if i == 'd':
        stack.append(stack[-1]*2)
    if i == '+':
        stack.append(stack[-1]+stack[-2])
print(sum(stack))  

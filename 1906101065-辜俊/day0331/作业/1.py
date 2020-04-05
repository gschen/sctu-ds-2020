class Bassball(object):
    def defen(self,x):
        stack = []
        for i in x:
            if i == '+':
                stack.append(stack[-1]+stack[-2])
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1]*2)
            else:
                stack.append(int(i))
        
        return sum(stack)

a = Bassball()
print(a.defen(['5','2','C','D','+']))
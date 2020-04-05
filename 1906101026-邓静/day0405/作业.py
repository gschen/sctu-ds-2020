class H():
    def y(self,c):
        result=[]
        for i in c:
            s=len(result)
            if i=="+":
                result.append(result[s-1]+result[s-2])
            elif i=="C":
                result.pop()
            elif i=="D":
                result.append(result[s-1]*2)
            else:
                result.append(int(i))
        return sum(result)
a=H()
print(a.y(["5","2","C","D","+"])) 
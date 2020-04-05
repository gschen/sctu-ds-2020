class Asd():
    def Sdf(self,zxc):
        result=[]
        for i in jie:
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
a=Asd()
print(a.Sdf(["5","2","C","D","+"]))
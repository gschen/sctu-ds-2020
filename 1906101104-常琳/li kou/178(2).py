class Solution:
    def f(self,votes):
        if len(votes)==1:
            return votes[0]
        n=len(votes[0])
        scor={}
        for i in range(len(votes)):
            for j in range(n):
                if votes[i][j] not in scor:
                    scor[votes[i][j]]=[0 for k in range(n)]
                    #0那个位置就是你要填充到[]里的内容，这里就表示我要填n个0进去，就是这样[0,0,0,0,0....]
                    scor[votes[i][j]][j]+=1
                else:
                    scor[votes[i][j]][j]+=1
        print(scor)
        scor=[p for p in sorted(scor.items(),key=lambda item:item[0])]
        print(scor)
        #将scor的value值按照升序进行排列，并转换成列表
        result=[p for p in sorted(scor,key=lambda item:[-item[1][m] for m in range(n)])]
        print(result)
        result1=''
        for i in result:
            result1+=i[0]
        print(result1)
        return result1
a=Solution()
a.f(['ABC','ACB','ABC','ACB','ACB'])

#sorted函数按照key值对字典排序：
d={'lilee':25,'wangyan':21,'liqun':32,'lidaming':19}
print(sorted(d.keys()))
#sorted函数按照value值对字典排序：
d={'lilee':25,'wangyan':21,'liqun':32,'lidaming':19}
print(sorted(d.items(),key=lambda item:item[1]))

s=[0 for i in range(3)]
print(s)



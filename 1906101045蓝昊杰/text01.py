class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n=len(votes)
        m=s=0
        l1=[]
        l2=[]
        if n==1 or len(set(votes))==1:
            return votes[0]
        for i in votes[0]:
            for j in range(len(votes[0])):
                for k in range(n):
                    if i==votes[k][m]:
                        s+=1
                l1.append(s)
                m+=1
                s=0
            m=0
            l2.append(l1)
            l1=[]
        if len(set(l2))==1:
            return sorted(votes[0])
        d={}
        for f in range(len(votes[0])):
            d[tuple(l2[f])]=votes[0][f]
        v=sorted(d.items(),reverse =True)
        l3=[]
        for g in v:
            l3.append(g[1])
        return "".join(l3)
    
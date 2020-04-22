class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        n=len(croakOfFrogs)
        a=0
        s="croak"
        nums=0
        l=[]
        q=0
        w=0
        e=0
        r=0
        t=0
        y=0
        for k in croakOfFrogs:
            if k=="c":
                q+=1
            elif k=="r":
                w+=1
            elif k=="o":
                e+=1
            elif k=="a":
                r+=1
            else:
                t+=1
        if q==w==e==r==t:
            y=1
        if y==0 or len(croakOfFrogs)%5!=0:
            return -1
        if croakOfFrogs=="croak"*(n//5):
            return 1
        for j in range(len(croakOfFrogs)):
            if croakOfFrogs[j]=="c":
                l.append(j)
        for h in l:
            for i in range(h,n):
                if croakOfFrogs[i]==s[a]:
                    a+=1
                if a==5:
                    nums+=1
                    a=0
                    break
        return nums
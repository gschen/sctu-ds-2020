#计算回退下标
def back_index(s):
    lis=[-1]
    k=-1
    for i in range(1,len(s)):
        if s[i]==s[k+1]:
            k+=1
        while s[i]!=s[k+1]:
            k=lis[k]
        lis.append(k)
    return lis
print(back_index('ababa'))
def kmp(s1,s2):#s1是母串，s2是子串
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
        #当k=len（s2）-1
        if k==len(s2)-1:
            lis.append(i)
            k=s2_lis[k]
    return lis
print(kmp('abaabcab','abc'))




        
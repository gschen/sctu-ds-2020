#-1代表没有，0代表有一个
c='aabcab'
[-1,0,-1,-1,1,0]
#计算回退下标
def back_index(s):
    lis=[-1]#代表第一个字符
    k=-1#最长公共前缀
    for i in range(1,len(s)):
        while s[i]!=s[k+1] and k>-1 :#不满足情况，需要不断回退，同时避免退到-1
            k=lis[k]
        if s[i]==s[k+1]:#满足情况，最长公共前缀加一
            k=k+1
        lis.append(k)
    return lis
print(back_index('ababacb'))

def kmp(s1,s2):#s1是母串，s2是子串
    s2_lis=back_index(s2)
    k=-1#代表的是相同序列的长度
    lis=[]
    for i in range(len(s1)):
        while k>-1 and s1[i]!=s2[k+1]:
            k=s2_lis[k]
        #相同序列
        if s1[i]==s2[k+1]:
            k=k+1
            #当k=len (s2)-1,匹配成功
        if k==len(s2)-1:
                lis.append(i)
                k=s2_lis[k]
    return lis

print(kmp('abaabcab','abc'))
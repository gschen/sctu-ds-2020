a='aba'
[-1,-1,0]#-1代表没有，0代表有一个，以此类推


#计算回退下标
def back_index(s):
    lis=[-1]#代表第一个字符
    k=-1#最长公共前缀
    for i in range(1,len(s)):
        if s[i]==s[k+1]#满足情况，最长公共前缀加1
        k=k+1
        while s[i]!=s[k+1] and k>-1:
            k=lis[k]
        lis.append(k)
    return lis
print(back_index('ababa'))

def kmp(s1,s2):
    s2_lis=back_index(s2)
    k=-1
    for i in range(len(s1)):
        while k>-1 and s1[i]!=s2[k+1:
            k=s2_lis[k]
        #相同序列
        if s1[i]==s2[k+1]:
            k=k+1
        #当k=len(s2)-1
        if k==len(s2)-1:
            lis.append(i)
            k=s2_lis[k]
    return lis
print(kmp('abaabcab','abc'))

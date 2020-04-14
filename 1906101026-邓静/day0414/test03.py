a='aba'
[-1,-1,0]#-1代表没有，0代表一个，以此类推
#计算回退下表
def back_index(s):
    lis=[-1]#代表第一个字符
    k=-1#最长公共前缀
    for i in range(1,len(s)):
        while s[i]!=s[k+1] and k>-1 :
            k=lis[k]

         if s[i]==s[k+1]:                           
             k=k+1
        lis.append(k)
    return lis
print(back_index('ababa'))
def kmp(s1,s2):
    s2_lis=back_index(s2)
    k=-1#代表的是相同的序列长度
    for i in range(len(s1)):
        #相同序列
        if s1[i]==s2[k+1]:
            k=k+1
        if k==len(s2)-1:
            lis.append(i)
    return lis
print(kmp('abaabcab','abc'))

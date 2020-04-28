a='aba'
[-1,-1,0]#-1代表没有，0代表1，以此类推
b='ababa'
[-1,-1,0,1,2]

#计算回退下标
def back_index(s):
    lis=[-1]#代表第一个字符
    k=-1#最长公共前缀
    for i in range(1,len(s)):
        if s[i]==s[k+1]:#满足情况，最长公共前缀加一
            k=k=1
        while s[i]!=s[k+1] and k >-1:#不满足情况，需要不断往后退到-1
            k=lis[k]
        lis.append(k)
    return lis
print(back_index('ababaca'))

def kmp(s1,s2):#s1是母串s2是子串
    s2_lis=back_index(s2)
    k=-1#代表相同的序列长度
    lis=[]
    for i in range(len(s1)):
        #需要回退的情况
        while k >-1 and s1[i]!=s2[k+1]:
            k=s2_lis[k]
        #相同序列 
        if s1[i]==s2[k+1]:
            k=k+1
        if k==len(s2)-1:
            lis.append(i)
    return lis

print(kmp('abaabcab','abc'))

'''给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水'''
def trap(height):
    #边界条件
    if len(height)<3:
        return 0
    n=len(height)
    lmax=[0]*n
    rmax=[0]*n
    ans=0
    #初始化左右峰
    lmax[0]=height[0]
    rmax[n-1]=height[n-1]
    #储存左右峰
    for i in range(1,n):
        lmax[i]=max(height[i],lmax[i-1])
    for j in range(n-2,-1,-1):
        rmax[j]=max(height[j],rmax[j+1])
    #遍历 比较每个位置可以存多少水
    for k in range(n):
        if min(rmax[k],lmax[k])>height[k]:
            ans+=min(rmax[k],lmax[k])-height[k]
    return ans
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
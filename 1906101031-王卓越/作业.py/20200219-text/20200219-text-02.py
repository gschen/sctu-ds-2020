# 2、	单利公式为：单利=（P x T x R）/ 100其中，P是本金T是时间，R是利率
# 例如输入：P = 10000
#       R = 5
#       T = 5
# 输出：2500
P,R,T=map(int,input().split())
interest=(P*T*R)/100
print(interest)

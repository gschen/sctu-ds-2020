#2、单利公式为：单利=（P x T x R）/ 100其中，P是本金，T是时间，R是利率,
# 例如输入：P = 10000 ,R = 5 ,T = 5,输出：2500
# 要求:P、T、R都是input输入的，不能固定。


P,T,R=map(int,input('分别输入本金，时间，利率：').split(','))
s=P*T*R/100
print('单利为：',s)
#单利公式为：单利=（P x T x R）/ 100其中，P是本金T是时间，R是利率
#例如输入：P = 10000
      #R = 5
      #T = 5
#输出：2500
#要求：T,P,R都是input输入
P=eval(input("请放入P值:"))
T=eval(input("请放入T值:"))
R=eval(input("请放入R值:"))
s=(P*T*R)/100
print(s)

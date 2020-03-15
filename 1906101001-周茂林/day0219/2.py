'''
单利公式为：单利=（P x T x R）/ 100其中，P是本金T是时间，R是利率
例如输入：P = 10000
      R = 5
      T = 5
输出：2500
要求:P、T、R都是input输入的，不能固定。
'''


def bbb(P, T, R):
    return (P*T*R) / 100


P, T, R = map(int, input().split())
print(bbb(P, T, R))

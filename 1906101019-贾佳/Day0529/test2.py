import numpy as np 

def LU_decomposition(A):
    n = len(A)
    L = np.zeros([n,n])
    U = np.zeros([n,n])

    for i in range(n):
        L[i][i] = 1
        if i == 0:
            U[0][:] = A[0][:]
            for j in range(1,n):
                L[j][0] = A[j][0] / U[0][0]
    return L,U
        # else:
        #     for j in range(1,n):
        #         temp = 0
        #         for k in range(j,n):


print(LU_decomposition([[2,2,3],
     [4,7,7],
     [-2,4,5]]))
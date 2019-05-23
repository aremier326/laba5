import matplotlib.pyplot as plt
import numpy as np
import random

def fillRandom(A):
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            A[i][j] = random.randint(0,1)
            if A[i][j] == 0:
                A[i][j] = -1

def izing(i, j, t):
    dE = 0
    if A[(i - 1) % N][(j) % N] == A[i][j]:
        dE += 2
    else:
        dE += -2

    if A[(i + 1) % N][(j) % N] == A[i][j]:
        dE += 2
    else:
        dE += -2

    if A[(i) % N][(j - 1) % N] == A[i][j]:
        dE += 2
    else:
        dE += -2

    if A[(i) % N][(j + 1) % N] == A[i][j]:
        dE += 2
    else:
        dE += -2

    if dE <= 0:
        A[i][j] = (-1) * A[i][j]
    else:
        R = float(random.randint(0, 10000)/10000)
        if R < np.exp(-dE / (K * t)):
            A[i][j] = (-1) * A[i][j]


#def energy():
#    E = 0
#    for i in range(0, len(A)):
#        for j in range(0, len(A[0])):
#            dE = 0
#            if A[(i-1) % N][(j)%N] == A[i][j]:
#                dE += -1
#            else:
#                dE += 1
#            if A[(i+1) % N][(j)%N] == A[i][j]:
#                dE += -1
#            else:
#                dE += 1
#            if A[(i)%N][(j-1)%N] == A[i][j]:
#                dE += -1
#            else: dE += 1
#            if A[(i)%N][(j+1)%N] == A[i][j]:
#                dE += -1
#            else:
#               dE += 1
#            E += dE
#            return abs(E);

M = []
N = 15
A = [[0] * N for i in range(N)]
K = 8.617*10**(-2)
T = []
E = []


for t in np.arange(0.001, 300, 0.1):
    fillRandom(A)
    for k in range(0, 2000):
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)
        izing(i, j, t)

    T.append(t)
    E.append(energy())
    S = 0

    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            S += A[i][j]

    M.append(abs(S/N))


plt.plot(T, E)
plt.xlabel('T')
plt.ylabel('M')
plt.grid()
plt.show()
from time import time
from numpy import sqrt, exp
from random import gauss, seed

seed(20000)
t0 = time()

S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2

M = 50
dt = T / M
I = 250000

S = []
for i in range(I):
    path = []
    for t in range(M + 1):
        if t == 0:
            path.append(S0)
        else:
            z = gauss(0.0, 1.0)
            St = path[t - 1] * exp((r - sigma ** 2 / 2) * dt + sigma * sqrt(dt) * z)
            path.append(St)
    S.append(path)

C0 = exp(-r * T) * sum([max(path[-1] - K, 0) for path in S]) / I
tpy = time() - t0

print("European Option Value {:7.3f}".format(C0))
print("Duration in Seconds {:7.3f}".format(tpy))
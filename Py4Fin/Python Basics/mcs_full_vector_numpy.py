import numpy as np
from time import time

np.random.seed(20000)
t0 = time()

S0 = 100
K = 105
T = 1.0
r = 0.05
sigma = 0.2

M = 50
dt = T / M
I = 250000

S = S0 * np.exp(np.cumsum((r - sigma ** 2 / 2) * dt
                    + sigma * np.sqrt(dt) * 
                    np.random.standard_normal((M + 1, I)), axis=0))
S[0] = S0

C0 = np.exp(-r * T) * np.sum(np.maximum(S[-1] - K, 0)) / I
tnp2 = time() - t0

print("European Option Value {:7.3f}".format(C0))
print("Duration in Seconds {:7.3f}".format(tnp2))
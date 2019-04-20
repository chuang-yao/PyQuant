import numpy as np
import matplotlib.pyplot as plt

np.random.seed(20000)

S0 = 100
K = 105
T = 1.0
r = 0.05
sigma = 0.2

M = 50
dt = T / M
I = 250000

S = S0 * np.exp(np.cumsum((r - sigma ** 2 / 2) * dt
    + sigma * np.sqrt(dt) * np.random.standard_normal((M + 1, I)), axis=0))
S[0] = S0

plt.plot(S[:, :10])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index level')
plt.show()

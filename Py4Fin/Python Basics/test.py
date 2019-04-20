from bsm_functions import bsm_call_value

S0 = 100.0
K = 105.0
T = 1.0
r = 0.05
sigma = 0.2

C = bsm_call_value(S0, K, T, r, sigma)
print("{:7.3f}".format(C))

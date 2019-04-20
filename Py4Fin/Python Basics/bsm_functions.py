def bsm_call_value(S0, K, T, r, sigma):
    from numpy import log, sqrt, exp
    from scipy.stats import norm

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + sigma ** 2 / 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0 / K) + (r - sigma ** 2 / 2) * T) / (sigma * sqrt(T))
    value = (S0 * norm.cdf(d1, 0.0, 1.0)
            - K * exp(-r * T) * norm.cdf(d2, 0.0, 1.0))

    return value


def bsm_vega(S0, K, T, r, sigma):
    from numpy import log, sqrt
    from scipy.stats import norm

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + sigma ** 2 / 2) * T) / (sigma * sqrt(T))
    vega = S0 * norm.cdf(d1, 0.0, 1.0) * sqrt(T)

    return vega


def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, itr=100):
    for i in range(itr):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0)
                / bsm_vega(S0, K, T, r, sigma_est))

    return sigma_est

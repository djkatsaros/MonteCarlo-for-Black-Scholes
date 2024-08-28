# Executes a basic monte carlo simulation for a lognormal random variable.
# INspired by the example of fluctuation assets (say stocks) in some supply
# and demand driven trading market

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def stock_MC(S0, mu, sig, N=1000):
    """
    S0:          initial stock price
    mu:          mean for S(t) lognormal distr
    sig:         stand. dev. for S(t) lognormal distr
    num_sims:    number of simulations, default = 100
    N:           number of samples in each simulation.
    """
    result = []
    for _ in range(num_sims): # number of simultions, S(t) realizations of the process
        prices = [S0]
        for _ in range(N):
            # sim the change day by day (t=1)
            stock_price = prices[-1]*np.exp((mu - 0.5 * sig ** 2) + sig * np.random.normal())
            prices.append(stock_price)
        result.append(prices)
        
    simul_data = pd.DataFrame(result)
        
    # given columns will contain the time series for a given simulation
    simul_data = simul_data.T
    # append the average (most probable trajectory) to the dataframe
    simul_data['mean'] = simul_data.mean(axis=1)

     print(simul_data)
     plt.plot(simul_data)
     plt.show()


if __name__ == "__main__":
    stock_MC(50,0.0002,0.01)

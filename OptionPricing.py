"""
Uses Monte Carlo simulation to price options via the Black-Scholes equation. 
From this we can compute the value of a call option (now) given the starting prices of
the underlying stocks, the strike price, the expiry time, risk free interest rate, and
the standard deviation for the underlying asset.

Also includes methods for directly computing this price via the Black-Scholes formula.

The main loop is written to compare these methods, first computing the option prices with 
the Monte Carlo sampling and then with the Black-Scholes formula. This MC sampling 
script is therefore essentially approximating the solution for the Black-Scholes equation.
"""
import numpy as np
from scipy import stats
from numpy import log, exp, sqrt


class OptionPricing:

    def __init__(self, S0, E, T, rf, sig, iterations):
        """
        S0:         starting price of the underlying asset (stock)
        E:          strike price
        T:          expiry time/time to maturity (days)
        rf:         risk free interest rate
        sig:        standard deviation
        iterations: number of MC iteration simulations
        """
        self.S0 = S0
        self.E = E
        self.T = T
        self.rf = rf
        self.sig = sig
        self.iterations = iterations

    def call_option_simulation(self):
        # 2 columns: first with 0s, 2nd will be payoffs
        # first column has 0s because the payoff function is max(0,S-E) (call option)
        option_data = np.zeros([self.iterations, 2])
        # 1 dimensional, size = num of iterations
        rand = np.random.normal(0,1,[1,self.iterations])

        #equation for S(t) stock price at T
        # drift + random piece from the Wiener process. 
        # creates an array
        stock_price = self.S0 * np.exp(self.T * (self.rf - 0.5 * self.sig ** 2) + self.sig * np.sqrt(self.T) * rand)
        
        # compute max(S-E,0)
        option_data[:, 1] = stock_price -self.E
        
        # average for the Monte-Carlo simulation
        average = np.sum(np.amax(option_data, axis=1))/float(self.iterations)

        # apply exp(-rT) discount factor.
        return np.exp(-1.0*self.rf*self.T)*average

    def put_option_simulation(self):
        # 2 columns: first with 0s, 2nd will be payoffs
        # first column has 0s because the payoff function is max(0,S-E) (call option)
        option_data = np.zeros([self.iterations, 2]) 
        #print(option_data)
        # 1 dimensional, size = num of iterations
        rand = np.random.normal(0,1,[1,self.iterations])

        # equation for S(t) stock price at T
        # drift + random piece from the Wiener process. 
        # creates an array
        stock_price = self.S0 * np.exp(self.T * (self.rf - 0.5 * self.sig ** 2) + self.sig * np.sqrt(self.T) * rand) 
    
        # compute now max(E-S,0) since now it's a put option
        option_data[:, 1] = self.E - stock_price

        #average for the Monte-Carlo simulation
        average = np.sum(np.amax(option_data, axis=1))/float(self.iterations)

        # apply exp(-rT) discount factor
        return np.exp(-1.0*self.rf*self.T)*average

    def call_option_price(self):#S, E, T, rf, sigma):
        """Directly compute from Black Scholes equation
        Gut check primarily """
        #d1 and d2 parameters
        d1 = (log(self.S0 / self.E) + (self.rf + self.sig * self.sig / 2.0) * self.T) / (self.sig * sqrt(self.T))
        d2 = d1 - self.sig * sqrt(self.T)
        print("The d1 and d2 parameters: %.4f, %.4f" % (d1, d2))
        # use the N(x) to calculate the price of the option
        return self.S0*stats.norm.cdf(d1)-self.E*exp(-self.rf*self.T)*stats.norm.cdf(d2)


    def put_option_price(self):#S, E, T, rf, sigma):
        """
        Directly compute from Black-Scholes equatoin
        """
        # compute d1 and d2 parameters
        d1 = (log(self.S0 / self.E) + (self.rf + self.sig * self.sig / 2.0) * self.T) / (self.sig * sqrt(self.T))
        d2 = d1 - self.sig * sqrt(self.T)
        print("The d1 and d2 parameters: %.4f, %.4f" % (d1, d2))
        # compute price of put option
        return -self.S0*stats.norm.cdf(-d1)+self.E*exp(-self.rf*self.T)*stats.norm.cdf(-d2) 

if __name__ == '__main__':
    model = OptionPricing(100, 100, 1, 0.05, 0.2, 10000)
    call_sim = model.call_option_simulation()
    put_sim = model.put_option_simulation()
    call_exct = model.call_option_price()
    put_exct = model.put_option_price()
    print('Value of the call option is  $%.2f' % call_sim)
    print('Value of the put option is  $%.2f' % put_sim)
    print('Direct call option price is $%.2f' % call_exct)
    print('Direct put option price is $%.2f' % put_exct)
    print('Error in call option price: $%f' % np.abs(call_sim - call_exct))
    print('Error in put option price: $%f' %np.abs(put_sim - put_exct))

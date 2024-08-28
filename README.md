# MonteCarlo-for-Black-Scholes

---------------------------------------------------------------------------------------------------------------------------
## General Background for Black Scholes

In finance, we have **unsystematic** and **systematic** risk. Unsystematic risk involves risk from the fluctuations in price of a held asset (asset prices _will_ oscillate due to changes in supply and demand).  Systematic risk involves risk from external factors such as war, recessions, changes in interest rates etc. In principle, it is hard to eliminate all risk. 

For example, we can diversify away unsystematic risk using portfolio optimization. This is the basic concept behind _Markowitz portfolio theory_: https://en.wikipedia.org/wiki/Modern_portfolio_theory. A rudimentary example for a 3 stock portfolio would be to optimize the percentage of the porfolio allocated to each stock such that we maximize our return for a given risk (measured using the volatility of the porfolio). This works best (generates the biggest return) when the stocks are _uncorrelated_ in such a way that a loss in one can be made up for by the gain in another. In this manner, one combines multiple risky assets into one portfolio to actualaly lower the risk of the whole portfolio.

Regardless of it's contents, the above Markowitz model inspired portfolio would still be subject to the systematic risk of the market fluctuations. 
This is what the _Capital Asset Pricing Model_ states. The _CAPM_ model along with tools from regression allows one to essentially measure the non-diversifiable risk by computing a parameter (commonly $\beta$) addressing the asset's sensitvity to non-diversifiable (aka systematic) risk. It does not make any effort to get rid of such risk, but rather is used to determine the appropriate pricing for a given security given the systematic/market risk.

The Black-Scholes model provides a pricing model for (European style) options that eliminates both these risks. It is known as a _market neutral strategy_, and proceeds in the following way. Consider a call option, i.e. the right to buy a specific asset a pre agreed upon price at a specified time $T$, referred to as the time to maturity or expiry. The call option will rise in value $V$ as the underlying assset rises in value and
vice versa as the payoff at time $T$ will be greater if the underlying price $S(t)$ is higher at $T$ $\Rightarrow$ these two quantities are positively correlated! With a put option, where the investor has a right to sell a stock at a pre agree upon price at $T$, there is a negative correlation between $V$ and $S(t)$. Focusing on call options, we may exploit this correlation to build a special portfolio.

Let the portfolio $\pi$ consist of a long position in the option $V(S,t)$, which we've seen depends on $S(t)$ and time $t$, and a short position of the same stock $S(t)$ parameterized by the parameter $\Delta$. 
Write the portfolio as $\pi = V(S,t) - \Delta S(t)$ because we are selling the short positon. $\Delta$ determines how much of the underlying asset $S(t)$ we are shorting. To figure out $\Delta$, we recall
that a **standard assumption in quant finance is that the underlying asset $S$ follows a lognormal random walk:** $dS = \mu S dt  + \sigma S dX$ where $\mu$ and $\sigma$ are the mean and standard deviation
respectively. For the whole portfolio, differentiate using Ito's Lemma (which is essentially a Taylor expansion) to obtain (after dropping higher order terms) $d\pi = dV(S,T) - \Delta dS  = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial S} dS
+\frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} dt - \Delta dS$, which we collect as
$d\pi = ( \frac{\partial V}{\partial t}  + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} ) dt + ( \frac{\partial V}{\partial S}  - \Delta) dS = [Deterministic~ part] + [Stochastic ~part ]$.
If we choose $\Delta = \frac{\partial V}{\partial S}$, we effectively reduce risk to $0$ since then the portfolio is totally deterministic! This delta changes with time, so this _"Delta Hedging"_ is an example of
so called _Dynamic Hedging_. Choosing $\Delta$ in this manner leaves us to solve
$d\pi = ( \frac{\partial V}{\partial t}  + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} ) dt$. However, the _no arbitrage principle_ says that the risk free change $d\pi$ must be the same as the growth we would get if we lend the same amount of money to the bank at the risk free interest rate $r$. This means $d\pi = r\pi dt$ as well, so plugging in for $\pi$ and $\Delta we now have
$d\pi = ( \frac{\partial V}{\partial t}  + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} ) dt = r(V-S\frac{\partial V}{\partial S} ) dt$, or
$\frac{\partial V}{\partial t}  + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - rV =0$, which is the **Black Scholes Equation** in all it's glory. It is a parabolic 
linear PDE, and has solution $S(0) N(d_1) - E e^{-r(T-t)} N(d_2)$ where $N(x) = \int_{-\infty}^x exp(-\frac{s^2}{2}) ds$, $E$ is the strike price (agreed upon price in the future), $d_1= \frac{ \log(\frac{S(0)}{E}) + (r+\frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}$ and $d_2=d_1- \sigma \sqrt{T-t}$. For a put option, the solution is instead $-S(0)N(-d_1) + E e^{-r(T-t)}N(-d_2)$.

In practice, the $\Delta$ parameter for a portfolio will be a sum of $w_i \cdot \Delta_i$'s where $\Delta_i = \frac{\partial V}{S_i}$ is the delta for a given stock in the portfolio, and $w_i$ is the proportion of that
option in the portfolio. One also talks about $\Gamma = \frac{\partial^2 V}{\partial S^2}$, which is the sensitivity of $\Delta$, being the rate of change of $\Delta$ (or some $\Delta_i$). This measures how often the position must be rehedged to maintain a delta-neutral position [meaning the portfolio value remains unchanged under small changes in the underlying asset(s)]. Writing also $\Theta = \frac{\partial V}{\partial t}$ for the rate of change of the option price with time, and 
$\mathscr{V} = \frac{\partial V}{\partial \sigma}$ for the change/volatility, we have the shorthand form for the Black-Scholes model:
$\Theta + \frac{1}{2} \sigma^2 S^2 \Gamma + r S \Delta  - r \mathscr{V} =0$. 

---------------------------------------------------------------------------------------------------------------------------
## Monte Carlo Simulation Example: Predicting Stock Evolutions 

The .py file titled **TODO**
contains a basic implementation of a monte carlo simulation to simulate the fluctuation in a stock price. 

Monte Carlo simulation essentially computes a ton of instances of some random variable with the average / most frequent value being a good prediction of the value of some (possibly deterministic) quantity.

![stockMC](https://github.com/user-attachments/assets/34ec6a6f-03b2-478e-a94e-20376f5b2d92)

The above image was generated using **TODO**.py. One knows that a stock price follows a lognormal distribution with $dS = \mu S dt + \sigma S dX$. This has solution $S(t) = S(0) e^{ (\mu - \frac{1}{2} \sigma^2)t + \sigma W_t}$, for $W$ a Wiener process with increments $W(t+dt) - W(t) \sim \mathcal{N}(0,dt)$ such that we can roughly assume $W_t \sim \mathcal{N}(0,dt)$ as well.

Generally, the algorithm goes like
1. Generate a number of samples from the formula for $S(t)$, which involves sampling from the random variable $W_t \sim \mathcal{N}(0,dt)$. This creates a time series for $(S(t)$. The formula for $S(t)$, which is a _geometric random walk_, provides the constraint for the MC sampling. 

2. Append the time series to a dataframe.

3. Compute the mean column-wise for the time series to get the trajectory with the highest probability.

We then plotted all the series as well as their mean.

---------------------------------------------------------------------------------------------------------------------------
## Application to Black-Scholes Model

The OptionPricing script contains an implementation of the Monte Carlo sampling technique. It also contains methods for directly computing the price using the Black-Scholes equation. If one tries both, then with a large enough number of iterations the Monte Carlo sampling gives the same value as the exact answer to high error. 

This gives the price of put and call options of given strike price, expiry, initial underlying asset value etc. One could easily generalize this to a weighted combination of stocks in a portfolio. 

---------------------------------------------------------------------------------------------------------------------------
## Repo Structure

This readme and the two scripts mentioned and described above.


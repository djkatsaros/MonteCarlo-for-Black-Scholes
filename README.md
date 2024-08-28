# MonteCarlo-for-Black-Scholes

---------------------------------------------------------------------------------------------------------------------------
## General Background

In finance, we have **unsystematic** and **systematic** risk. Unsystematic risk involves risk from the fluctuations in price of a held asset (asset prices _will_ oscillate due to changes in supply and demand.  Systematic risk involves risk from external factors such as war, recessions, changes in interest rates etc. In principle, it is hard to eliminate all risk. 

For example, we can diversify away unsystematic risk using portfolio optimization. This is the basic concept behind _Markowitz portfolio theory_: https://en.wikipedia.org/wiki/Modern_portfolio_theory. A rudimentary example for a 3 stock portfolio would be to optimize the percentage of the porfolio allocated to each stock such that we maximize our return for a given risk (measured using the volatility of the porfolio). This works best (generates the biggest return) when the stocks are _uncorrelated_ in such a way that a loss in one can be made up for by the gain in another. Regardless of it's contents, this portfolio would still be subject to the systematic risk of the market fluctuations. 

The _Capital Asset Pricing Model_ can be used along with tools from regression to compute a parameter (commonly \beta) addressing the asset's sensitvity to non-diversifiable (aka systematic) risk. It does not make any effort to get rid of such risk, but rather is used to determine the appropriate pricing for a given security.

The Black-Scholes model provides a pricing model for (European style) options that eliminates both these risks in the following way. 

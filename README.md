# ROIC Regression

In order to determine if ROIC is a good indicator of a company's (future) performance, a linear regression has been run on past data in the form of supervised learning. The variables that were identified to pertain to a company’s return were the ROIC, FCF (Free Cash Flow) and Debt Equity. 

However, the ROIC values were not used directly –– a better implementation was to look at the trend of ROIC. Therefore, a linear regression was first run on the ROIC values from year 2014-2019. The slope and the R^2 value of that regression is saved to use as parameters (the y-intercept value is arbitrary).

Combining the rate of change of ROIC, its corresponding R^2 value, FCF and Debt Equity, a multivariable linear regression was ran against the 5 year return per annum from 2014 to 2019. The resulting equation is:

```5Y_RETURN_PA = 3.76 * ROIC_SLOPE + 6.93 * R_SQUARED + 0.16 * FCF + -0.03 * DEBT_EQUITY```

This model returned an R^2 value of 0.15, which does seem low at first. However, we must take into account this score is determining the accuracy of the model in predicting the exact value of 5Y return, not whether it is a positive return or a negative one. Running this model on another set of testing data, it correctly predicted that 60 out of 90 companies would have a positive return, which gives a 66.7% success rate.

______________________________________________________________________________________________________________________


To further improve this model, we also looked at how sectors and market cap affected this model –– nuances between sectors and their respective orthodox business structures could elucidate another exploitable pattern. Splitting ROIC data from 2014-2019 into their respective sectors, a unique and separate linear regression was ran on each sector’s companies, using one more parameter than the last model –– market cap. 

Note: some data cleaning was done in order to match the order of magnitudes of the coefficients: The px change was all multiplied by 100 (due to it being a percentage) and market cap was divided by 1000.

Sectors with less than five companies were excluded, for reasons obvious.


Results are listed below:

Note: The coefficients are in the order of [ mkt_cap, roic_slope, r_squared, fcf, debt_equity ], and some are in scientific notation



=====================================



sector:  Auto Manufacturers

num of samples:  8

regression score:  0.9327277179356407

regression coefficients:  [  2.39661779  45.51475457 -64.82449236   3.81768043  -3.92349518]

 

=====================================

 

sector:  Building Materials

num of samples:  8

regression score:  0.5669509608033617

regression coefficients:  [-0.1462806  -9.83182192 23.71082434  2.49856977 -0.30982951]

 

=====================================

 

sector:  Chemicals

num of samples:  5

regression score:  1.0

regression coefficients:  [ -15.31738713   -7.85097927 -961.69143468  -12.55524638   -8.50839759]

 

=====================================

 

sector:  Commercial Services

num of samples:  9

regression score:  0.5682406389496031

regression coefficients:  [  0.61817783  48.56024178 -76.44196877  10.3482198   -0.85866465]

 

=====================================

 

sector:  Diversified Finan Serv

num of samples:  10

regression score:  0.8278773179337966

regression coefficients:  [ 4.08132029e-03  1.93958655e+01  1.98639821e+01 -4.36117182e-01

 -1.22136612e-01]

 

=====================================

 

sector:  Electric

num of samples:  11

regression score:  0.5492004063925908

regression coefficients:  [ 0.09744063  5.04807888  8.02518606  0.3443168  -0.25506307]

 

=====================================

 

sector:  Engineering&Construction

num of samples:  9

regression score:  0.7796960718777507

regression coefficients:  [ 0.23072268 33.10211192 47.33434432  0.18564733 -0.53816625]

 

=====================================

 

sector:  Food

num of samples:  8

regression score:  0.87672809691806

regression coefficients:  [  -0.35718289  122.83012356 -167.0162216     3.72753839   -0.78662024]

 

=====================================

 

sector:  Gas

num of samples:  6

regression score:  1.0

regression coefficients:  [  0.22692089 -29.82131744  78.90177686  19.39823093   2.79325593]

 

=====================================

 

sector:  Healthcare-Products

num of samples:  5

regression score:  1.0

regression coefficients:  [  0.14334917  -7.95716705   4.69762472 -21.63364196   0.04988758]

 

=====================================

 

sector:  Lodging

num of samples:  9

regression score:  0.5097811327870264

regression coefficients:  [-0.06304263 12.67918619 21.72014214  4.30442453  0.0582915 ]

 

=====================================

 

sector:  Mining

num of samples:  10

regression score:  0.4253369275611365

regression coefficients:  [  0.36772974  -3.99127921 -46.24742393  -0.08269716  -0.19758173]

 

=====================================

 

sector:  Oil&Gas

num of samples:  6

regression score:  1.0

regression coefficients:  [ 2.02204398e-01  5.00444665e+02 -2.11204962e+03  2.51607068e+01

  1.52276496e+01]

 

=====================================

 

sector:  Pharmaceuticals

num of samples:  14

regression score:  0.5029558229440583

regression coefficients:  [ 0.96285631 18.29935631 54.33780763  0.66164041  0.22089044]

 

=====================================

 

sector:  Real Estate

num of samples:  53

regression score:  0.07733241189085416

regression coefficients:  [  0.43866428  -4.13481359 104.85980806   0.38897351   1.07287224]

 

=====================================

 

sector:  Retail

num of samples:  16

regression score:  0.7812404530816045

regression coefficients:  [-4.52139189e-02  7.11536837e+01  2.44530402e+02  2.68132828e+00

  3.64136258e-01]

 

=====================================

 

sector:  Software

num of samples:  7

regression score:  0.9828590189257808

regression coefficients:  [ 6.97096295e-02  6.91842394e+00 -9.16582745e+01  3.56804445e+00

  1.19373344e+00]

 

=====================================

 

sector:  Telecommunications

num of samples:  7

regression score:  0.942321641262012

regression coefficients:  [ -0.04323938 -15.51140084  -8.20834249 -10.8258938    0.19478351]

 

=====================================

 

sector:  Transportation

num of samples:  7

regression score:  0.9869545300787287
regression coefficients:  [ 2.23463843e-01  3.80070194e+01  1.42954852e+02 -7.20047667e-01
 -1.18271439e-01]
=====================================

 

A quick look at the regression score for these models tell us that splitting into sectors does in fact give a higher accuracy in predicting the return/px change, with some scores exceeding 0.98. However, we must be cognisant of the fact that the less samples there are, the easier a model can account for all of them, as the samples do not accurately represent the population.

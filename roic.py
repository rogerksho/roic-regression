import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
import math
import numpy as np
from sklearn import linear_model

STD_CUTOFF = 6

def pearson_r(x, y):
   # Compute correlation matrix
   corr_mat = np.corrcoef(x, y)

   # Return entry [0,1]
   return corr_mat[0,1]


class Company:
    def __init__(self, debt_equity, fcf, roic_2014, roic_2015, roic_2016, roic_2017, roic_2018, roic_2019, return_annum):
        self.debt_equity = debt_equity
        self.fcf = fcf
        self.roic_slope, self.r_squared = self.compute_values(roic_2014, roic_2015, roic_2016, roic_2017, roic_2018, roic_2019)
        self.return_annum = return_annum

    def compute_values(self, *args):
        y = list()

        for i in args:
            if not math.isnan(i):
                y.append(i)
        
        x = [*range(len(y))]

        roic_slope = np.polyfit(x, y, 1)[0]
        r_squared = pow(pearson_r(x, y), 2)

        return roic_slope, r_squared


df = pd.read_excel(r'data.xlsx', sheet_name=0, usecols=[2,3,5,6,7,8,9,10,14])

company_list = list()

for i in df.values.tolist():
    company_list.append(Company(*i))

independent = list()
dependent = list()

for i in company_list:
    independent.append([i.roic_slope, i.r_squared, i.fcf, i.debt_equity])
    dependent.append(i.return_annum)

regr = linear_model.LinearRegression()
regr.fit(independent, dependent)
print('regression score: ', regr.score(independent, dependent))

print('regression coefficients: ', regr.coef_)


testing_df = pd.read_excel(r'data_testing.xlsx', sheet_name=0, usecols=[2,3,4,5,6,7,8,9,10])

company_list_test = list()

ctr = 0

def testing_func(company):
    prediction = regr.predict([[company.roic_slope, company.r_squared, company.fcf, company.debt_equity]])
    if prediction > 0:
        if company.return_annum > 0:
            return True
        elif company.return_annum < 0:
            return False

    if prediction < 0:
        if company.return_annum < 0:
            return True
        elif company.return_annum > 0:
            return False

for i in testing_df.values.tolist():
    company_list_test.append(Company(*i))

print('size of sample: ', len(company_list_test))

for i in company_list_test:
    if testing_func(i):
        ctr += 1
    else:
        pass

print('ctr: ', ctr)
    
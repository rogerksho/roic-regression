import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
import math
import numpy as np
from sklearn import linear_model
from collections import defaultdict

STD_CUTOFF = 6

def pearson_r(x, y):
   # Compute correlation matrix
   corr_mat = np.corrcoef(x, y)

   # Return entry [0,1]
   return corr_mat[0,1]


class Company:
    def __init__(self, sector, mkt_cap, debt_equity, fcf, roic_2014, roic_2015, roic_2016, roic_2017, roic_2018, roic_2019, px_change):
        self.sector = sector
        self.mkt_cap = mkt_cap/1000
        self.debt_equity = debt_equity
        self.fcf = fcf
        self.roic_slope, self.r_squared = self.compute_values(roic_2014, roic_2015, roic_2016, roic_2017, roic_2018, roic_2019)
        self.px_change = px_change*100

    def compute_values(self, *args):
        y = list()

        for i in args:
            if not math.isnan(i):
                y.append(i)
        
        x = [*range(len(y))]

        roic_slope = np.polyfit(x, y, 1)[0]
        r_squared = pow(pearson_r(x, y), 2)

        return roic_slope, r_squared


df = pd.read_excel(r'data_sector.xlsx', sheet_name=1, usecols=[2,3,4,5,6,7,8,9,10,11,12])

company_list = list()

# create list of companies
for i in df.values.tolist():
    company_list.append(Company(*i))

# sort companies by sector
company_dict = defaultdict(list)

for obj in company_list:
    company_dict[obj.sector].append(obj)

for ix, sector in company_dict.items():
    # independent and dependent variable
    independent = list()
    dependent = list()

    if len(sector) < 5:
        continue

    for company in sector:
        independent.append([company.mkt_cap, company.roic_slope, company.r_squared, company.fcf, company.debt_equity])
        dependent.append(company.px_change)

    regr = linear_model.LinearRegression()
    regr.fit(independent, dependent)

    print('sector: ', ix)
    print('num of samples: ', len(sector))
    print('regression score: ', regr.score(independent, dependent))

    print('regression coefficients: ', regr.coef_)
    print(' ')
    print('=====================================')
    print(' ')


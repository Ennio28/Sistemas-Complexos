import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

'''
This data correspond the confirmed cases of covid-19 by ARS, which is the health region area. 
Use  it to create a model for each ARS. What can you conclude?

Source: https://github.com/dssg-pt
  
'''

my_data = np.genfromtxt('covid_ars.csv', delimiter=',', skip_header=1)
cases = my_data[:, 2: ]
# The code bellow corresponds to the cases of the Center Region. You can consult the original dataset to see the
# different columns
x_values = np.arange(cases.shape[0])
cases_centro = cases[:, 1]

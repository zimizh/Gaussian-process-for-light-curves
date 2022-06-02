# plots and saves time series data

import os
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("error")

directory = 'light_curves_fausnaugh'

for filename in os.listdir(directory):
    f = pd.read_csv(os.path.join(directory, filename), delim_whitespace=True)
    
    time = f['BTJD']
    count = f['cts']
    uncertainty = f['e_cts']
    
    plt.errorbar(time, count, yerr = uncertainty, fmt = '.')
    plt.savefig(os.path.join('light_curves_plot', filename))

    plt.clf()





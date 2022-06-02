# plots and saves time series data

import os
import pandas as pd
import matplotlib.pyplot as plt

directory = 'light_curves_fausnaugh'

for filename in os.listdir(directory):
    f = pd.read_csv(os.path.join(directory, filename), delim_whitespace=True)
    
    time = f['BTJD']
    count = f['cts']
    background = f['bkg_model']
    uncertainty = f['e_cts']
    
    plt.errorbar(time, count-background, yerr = uncertainty, fmt = '.')
    plt.xlabel('BTJD')
    plt.ylabel('counts (- background)')
    plt.savefig(os.path.join('light_curves_plot', filename), bbox_inches = "tight")

    plt.clf()

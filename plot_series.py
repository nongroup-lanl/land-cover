"""
Plotting timeseries
"""

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from plot_utils import initialize_plot_settings

initialize_plot_settings()


def fix_ee_dataframe(df):
    pass

if __name__ == "__main__":
    filename = 'data/mamore_modis.csv'
    columns = ['crop', 'forest']
    labels = ['Cropland or built up', 'Forest']
    colors = ['#7570b3', '#1b9e77']

    df = pd.read_csv(filename)
    year = df['year']
    
    fig, ax = plt.subplots(1, 1, figsize=(8, 4))

    for var, lab, col in zip(columns, labels, colors):
        y = df[var]
        ax.plot(year, y, marker='s', color=col, label=lab)

    ax.set_xlabel('Year')
    ax.set_ylabel('Number of pixels')
    plt.legend(title='Land cover category')

    f = filename.split('/')[-1].replace('csv', 'png')
    plt.savefig('fig/' + f, dpi=150, bbox_inches='tight')

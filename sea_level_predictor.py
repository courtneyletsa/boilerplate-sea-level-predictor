import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)


    # Create first line of best fit
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))  # Extended to 2050
    y_pred = res_full.slope * x_pred + res_full.intercept
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line (1880–2050)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent_pred = pd.Series(range(2000, 2051))
    y_recent_pred = res_recent.slope * x_recent_pred + res_recent.intercept
    plt.plot(x_recent_pred, y_recent_pred, 'g', label='Best Fit Line (2000–2050)')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

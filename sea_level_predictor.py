import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # Create first line of best fit
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = pd.Series([i for i in range(1880, 2051)])
    line1 = reg1.slope * years_extended + reg1.intercept

    plt.plot(years_extended, line1, 'r', label='Best Fit Line 1 (1880-2050)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    reg2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_recent = pd.Series([i for i in range(2000, 2051)])
    line2 = reg2.slope * years_recent + reg2.intercept

    plt.plot(years_recent, line2, 'green', label='Best Fit Line 2 (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

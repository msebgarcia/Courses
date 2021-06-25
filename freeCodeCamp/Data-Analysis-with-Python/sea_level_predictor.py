import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
	# Read data from file
	df = pd.read_csv(r'epa-sea-level.csv',float_precision='legacy')

	# Create scatter plot
	fig,axes = plt.subplots(figsize=(11,8))
	plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'], label='Original Data')
	
	
	# Create first line of best fit
	slope1,intercept1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[:2]
	xYear1 = list(range(df['Year'][0],2050))
	yLevel1 = [(slope1*x+intercept1) for x in xYear1]
	plt.plot(xYear1, yLevel1, 'r', label='Fitted Line - All data')
	
	# Create second line of best fit
	slope2,intercept2 = linregress(df[df['Year']>=2000]['Year'], df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])[:2]
	xYear2 = list(range(2000,2050))
	yLevel2 = [(slope2*x+intercept2) for x in xYear2]
	plt.plot(xYear2, yLevel2, 'g', label='Fitted Line - Year >= 2000')
	
	# Add labels and title
	axes.grid()
	axes.set_xlabel('Year')
	axes.set_ylabel('Sea Level (inches)')
	axes.set_title('Rise in Sea Level')
	axes.legend()
	
	# Save plot and return data for testing (DO NOT MODIFY)
	plt.savefig('sea_level_plot.png')
	return plt.gca()
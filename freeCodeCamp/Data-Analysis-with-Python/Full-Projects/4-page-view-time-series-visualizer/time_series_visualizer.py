import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r'fcc-forum-pageviews.csv',index_col=0,names=['value'],skiprows=1,parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
		# Draw line plot
		fig = df.plot(figsize=(15,6)).figure
		plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
		plt.xlabel('Date')
		plt.ylabel('Page Views')

		# Save image and return fig (don't change this part)
		fig.savefig('line_plot.png')
		return fig

def draw_bar_plot():
		# Copy and modify data for monthly bar plot
		df_bar = df.groupby([(df.index.year),(df.index.month)]).mean().unstack()
		months = ['January','February','March','April','May','June','July','August','September','October','November','December']

		# Draw bar plot
		fig = df_bar.plot(kind='bar',figsize=(15,7)).figure
		plt.xlabel('Years')
		plt.ylabel('Average Page Views')
		plt.legend(labels=months)  

		# Save image and return fig (don't change this part)
		fig.savefig('bar_plot.png')
		return fig

def draw_box_plot():
		# Prepare data for box plots (this part is done!)
		df_box = df.copy()
		df_box.reset_index(inplace=True)
		df_box['year'] = [d.year for d in df_box['index']]
		df_box['month'] = [d.strftime('%b') for d in df_box['index']]

		# Draw box plots (using Seaborn)
		fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,6))
		sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
		ax1.set_title('Year-wise Box Plot (Trend)')
		ax1.set_xlabel('Year')
		ax1.set_ylabel('Page Views')

		months = df_box['month'].drop_duplicates().to_list()[8:]+df_box['month'].drop_duplicates().to_list()[:8]
		sns.boxplot(x="month", y="value", data=df_box, ax=ax2, order=months)
		ax2.set_title('Month-wise Box Plot (Seasonality)')
		ax2.set_xlabel('Month')
		ax2.set_ylabel('Page Views')

		# Save image and return fig (don't change this part)
		fig.savefig('box_plot.png')
		return fig

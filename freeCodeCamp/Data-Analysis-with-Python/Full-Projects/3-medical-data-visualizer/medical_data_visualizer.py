import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(r'medical_examination.csv')

# Add 'overweight' column

df['overweight'] = np.where((df['weight']/((df['height']/100)**2)) > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['gluc'] = np.where(df['gluc'] == 1,0,1)
df['cholesterol'] = np.where(df['cholesterol'] == 1,0,1)

# Draw Categorical Plot
def draw_cat_plot():
		# Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
		df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])

		# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
		#df_cat = None

		# Draw the catplot with 'sns.catplot()'
		fig = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')
		fig.set_ylabels('total')
		fig.set_xlabels('variable')
		# Do not modify the next two lines
		fig.savefig('catplot.png')
		return fig.fig


# Draw Heat Map
def draw_heat_map():
		# Clean the data
		c1 = df['ap_lo'] <= df['ap_hi']
		c2 = df['height'] >= df['height'].quantile(0.025)
		c3 = df['height'] <= df['height'].quantile(0.975)
		c4 = df['weight'] >= df['weight'].quantile(0.025)
		c5 = df['weight'] <= df['weight'].quantile(0.975)
		df_heat = df[c1 & c2 & c3 & c4 & c5]

		# Calculate the correlation matrix
		corr = df_heat.corr().round(1)

		# Generate a mask for the upper triangle
		mask = np.zeros_like(corr)
		mask[np.triu_indices_from(mask)] = True

		# Set up the matplotlib figure
		fig, ax = plt.subplots(figsize=(10,10),dpi=200)

		# Draw the heatmap with 'sns.heatmap()'
		sns.heatmap(corr, mask=mask, square=True, annot=True, linewidths=.5,cmap='magma', cbar_kws={"shrink": .50},fmt='.1f')
	

		# Do not modify the next two lines
		fig.savefig('heatmap.png')
		return fig

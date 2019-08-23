import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Read the data
data = 'gapminder-FiveYearData.csv'
td = pd.read_csv(data)
td.head()


#pivot table
table = pd.pivot_table(td, values='lifeExp', index=['year'],
                    columns=['continent'], aggfunc=np.sum)
table


# Compute the correlation matrix
corr = table.corr()
#Visualize the correlation using seaborn: Please refer to https://seaborn.pydata.org/examples/many_pairwise_correlations.html

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
f.savefig('corr.png', dpi=400)


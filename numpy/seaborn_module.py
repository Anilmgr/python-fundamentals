## Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
## pip install seaborn
## Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()
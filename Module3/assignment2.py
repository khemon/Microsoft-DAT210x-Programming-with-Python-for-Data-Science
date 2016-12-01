import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
from bokeh.charts.attributes import marker

matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
data_set = pd.read_csv('Datasets/wheat.data')


#
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 
data_set.plot.scatter(x='area', y='perimeter', marker='o')


#
# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
data_set.plot.scatter(x='groove', y='asymmetry', marker='.')


#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
data_set.plot.scatter(x='compactness', y='width', marker='^')



# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()


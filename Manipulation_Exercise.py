import os
import sys
import pandas as pd
import seaborn as sns


region = sys.argv[1]

countries = pd.read_csv('./python4sci-main/data/countries.csv')
pd.DataFrame(countries)
selection = countries.loc[countries['world_6region'] == region].set_index('name')
axes = selection["life_expectancy"].plot.bar()
figure = axes.get_figure()
figure.savefig('Expectancy.png', dpi=100)

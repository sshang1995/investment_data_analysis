import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
print(data.head())
life_expectancy = data['Life Expectancy']

#calculate quantiles
life_expectancy_quartiles = np.quantile(life_expectancy,[0.25,0.5,0.75])

plt.hist(life_expectancy)
for i in range(len(life_expectancy_quartiles)):
  plt.axvline(x=life_expectancy_quartiles[i],alpha=0.5, color='r')
plt.show()

gdp = data['GDP']

median_gdp = np.quantile(gdp,0.5)
print(median_gdp)

low_gdp =data[data['GDP']<=median_gdp]
high_gdp = data[data['GDP']>median_gdp]

low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'],[0.25,0.5,0.75])

high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'],[0.25,0.5,0.75])

print(low_gdp_quartiles)
print(high_gdp_quartiles)

plt.close()
plt.hist(high_gdp['Life Expectancy'],alpha = 0.5, label='High GDP')
for i in range(len(high_gdp_quartiles)):
  plt.axvline(x=high_gdp_quartiles[i],alpha=0.5, color='r')

plt.hist(low_gdp['Life Expectancy'],alpha = 0.5, label = 'Low GDP')

for i in range(len(low_gdp_quartiles)):
  plt.axvline(x=low_gdp_quartiles[i],alpha=0.5, color='g')
plt.legend()
plt.show()


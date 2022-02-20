# step_01 import library
import pandas as pd

# import data from file
data = pd.read_csv("generic-food.csv")

print(data)

import seaborn as sns
import matplotlib.pyplot as plt 
sns.set_theme(style="ticks", color_codes=True)
p= sns.countplot(x="GROUP", hue="FOOD_NAME", data=data)
plt.show()

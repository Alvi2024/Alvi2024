import pandas as pd
import matplotlib.pyplot as plt

# Reading the  dataset
df1 = pd.read_csv("food-hygiene-ratings-website-top-pages-december-2016-to-february-2017.csv")



# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df1['Pageviews'], df1['UniquePageviews'])
plt.title('Pageviews vs UniquePageviews')
plt.xlabel('Pageviews')
plt.ylabel('UniquePageviews')
plt.grid(True)
plt.tight_layout()
plt.show()

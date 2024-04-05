import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset with 'ISO-8859-1' encoding
df = pd.read_csv("Invoices-over-25k-April-2023.csv", encoding='ISO-8859-1')



# Plotting
plt.figure(figsize=(10, 6))
plt.hist(df['Amount in Sterling'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Amounts in Sterling')
plt.xlabel('Amount in Sterling')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

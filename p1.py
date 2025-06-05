import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv(r"C:\Users\Admin\Downloads\Housing.csv")
bins = [0, 25_00_000, 50_00_000, 75_00_000, 100_00_000, float('inf')]
labels = ['0-25L', '26-50L', '51-75L', '76-100L', '>100L']
df['price_range'] = pd.cut(df['price'], bins=bins, labels=labels, right=True)
price_range_counts = df['price_range'].value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.plot(price_range_counts.index, price_range_counts.values, marker='o', linestyle='-')
plt.title('Number of Houses in Each Price Range')
plt.xlabel('Price Range (in Lakhs)')
plt.ylabel('Number of Houses')
plt.grid(True)
plt.tight_layout()
plt.show()
print("House counts by price range:\n", price_range_counts)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 1. Sales by Region
plt.figure(figsize=(8, 5))
sns.barplot(x='Region', y='Sales', data=df, estimator=sum, ci=None, palette='Blues_d')
plt.title('Total Sales by Region')
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.close()

# 2. Profit by Sub-Category
plt.figure(figsize=(10, 6))
profit_plot = df.groupby('Sub-Category')['Profit'].sum().sort_values()
profit_plot.plot(kind='bar', color='tomato')
plt.title('Profit by Sub-Category')
plt.ylabel('Total Profit')
plt.tight_layout()
plt.savefig('profit_by_subcategory.png')
plt.close()

# 3. Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(12, 5))
monthly_sales.plot()
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
plt.close()

# 4. Discount vs Profit
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Discount', y='Profit', alpha=0.6, color='purple')
plt.title('Discount vs Profit')
plt.tight_layout()
plt.savefig('discount_vs_profit.png')
plt.close()

# 5. Segment-wise Profit Share
segment_profit = df.groupby('Segment')['Profit'].sum()
plt.figure(figsize=(6, 6))
segment_profit.plot.pie(autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'salmon'])
plt.title('Profit Share by Segment')
plt.ylabel('')
plt.tight_layout()
plt.savefig('profit_by_segment.png')
plt.close()

print("✅ All visualizations saved successfully!")

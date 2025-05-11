import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.style.use('dark_background')
file_path = r'D:\products.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)
# Convert Price column to numeric (cleaning '$' sign and converting to float)
df['Price'] = df['Price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
# Add additional columns if needed, e.g., total value = price * stock
df['TotalValue'] = df['Price'] * df['Stock']

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Category', y='Price', palette='muted')
plt.title('Price Distribution by Product Category', fontsize=16, color='white')
plt.xlabel('Category', fontsize=14, color='white')
plt.ylabel('Price ($)', fontsize=14, color='white')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Stock', y='Price', hue='Category', palette='muted')
plt.title('Stock vs Price by Category', fontsize=16, color='white')
plt.xlabel('Stock', fontsize=14, color='white')
plt.ylabel('Price ($)', fontsize=14, color='white')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Brand (Company)', y='Views', palette='muted')
plt.title('Total Views by Brand', fontsize=16, color='white')
plt.xlabel('Brand', fontsize=14, color='white')
plt.ylabel('Total Views', fontsize=14, color='white')
plt.xticks(rotation=45, ha='right', color='white')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Product Name', y='Stock', palette='muted')
plt.title('Stock Distribution by Product', fontsize=16, color='white')
plt.xlabel('Product Name', fontsize=14, color='white')
plt.ylabel('Stock', fontsize=14, color='white')
plt.xticks(rotation=45, ha='right', color='white')
plt.tight_layout()
plt.show()

category_value = df.groupby('Category')['TotalValue'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=category_value, x='Category', y='TotalValue', palette='muted')
plt.title('Total Product Value by Category', fontsize=16, color='white')
plt.xlabel('Category', fontsize=14, color='white')
plt.ylabel('Total Value ($)', fontsize=14, color='white')
plt.tight_layout()
plt.show()

top_products_by_views = df.nlargest(10, 'Views')
plt.figure(figsize=(12, 6))
sns.barplot(data=top_products_by_views, x='Product Name', y='Views', palette='muted')
plt.title('Top 10 Products by Views', fontsize=16, color='white')
plt.xlabel('Product Name', fontsize=14, color='white')
plt.ylabel('Views', fontsize=14, color='white')
plt.xticks(rotation=45, ha='right', color='white')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Price', bins=10, kde=True, color='orange')
plt.title('Price Distribution Across All Products', fontsize=16, color='white')
plt.xlabel('Price ($)', fontsize=14, color='white')
plt.ylabel('Frequency', fontsize=14, color='white')
plt.tight_layout()
plt.show()

category_counts = df['Category'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%',
        colors=sns.color_palette("muted", len(category_counts)), startangle=140, textprops={'color': 'white'})
plt.title('Product Category Distribution', fontsize=16, color='white')
plt.axis('equal')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 8))
corr_matrix = df[['Price', 'Stock', 'Views', 'TotalValue']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix', fontsize=16, color='white')
plt.tight_layout()
plt.show()

product_popularity = df[['Product Name', 'Views']].sort_values(by='Views', ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(data=product_popularity, x='Product Name', y='Views', palette='muted')
plt.title('Top 10 Most Popular Products by Views', fontsize=16, color='white')
plt.xlabel('Product Name', fontsize=14, color='white')
plt.ylabel('Views', fontsize=14, color='white')
plt.xticks(rotation=45, ha='right', color='white')
plt.tight_layout()
plt.show()


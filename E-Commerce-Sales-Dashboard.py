import pandas as pd
import matplotlib.pyplot as plt
import random

# 1. MESSY DATA BANAO
products = ['Laptop', 'Mobile', 'Headphones', 'T-Shirt', 'Shoes']
cities = ['Multan', 'Lahore', 'Karachi', 'Islamabad', 'Faisalabad']

data = []
for i in range(100):
    data.append({
        'Order_ID': f'ORD{1000+i}',
        'Product': random.choice(products),
        'City': random.choice(cities),
        'Sales': random.randint(5000, 80000),
        'Quantity': random.randint(1, 5)
    })

df = pd.DataFrame(data)

# Messy kar diya
df.loc[5, 'Sales'] = None
df.loc[10, 'City'] = 'multan'
df.loc[15, 'Product'] = 'laptop '

print("--- MESSY DATA ---")
print(df.head(10))

# 2. CLEANING - Sirf 3 line!
df['Product'] = df['Product'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()
df['Sales'] = df['Sales'].fillna(df['Sales'].median())

print("\n--- CLEAN DATA ---")
print(df.head(10))

# 3. ANALYSIS
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False)

print("\nTOP PRODUCT:")
print(product_sales)
print("\nTOP CITY:")
print(city_sales)

# 4. GRAPH
plt.figure(figsize=(8,5))
product_sales.plot(kind='bar', color='#00D1FF')
plt.title('Total Sales by Product - BOSS Project', fontweight='bold')
plt.ylabel('Sales (Rs)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
city_sales.plot(kind='bar', color='#FF6B00')
plt.title('Total Sales by City', fontweight='bold')
plt.ylabel('Sales (Rs)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
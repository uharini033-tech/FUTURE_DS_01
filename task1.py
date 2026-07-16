import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Correct File Name
file_name = 'Sample - Superstore.csv'

if not os.path.exists(file_name):
    print(f"Error: '{file_name}' file unga folder-la illa! Check pannunga.")
    exit()

# Encoding standard format
df = pd.read_csv(file_name, encoding='windows-1252')

print("--- DATASET READY ---")
print(f"Total Rows: {df.shape[0]} | Total Columns: {df.shape[1]}")

# Column names spaces-ah clean pandrom
df.columns = df.columns.str.strip()

# 2. DATA CLEANING
df = df.dropna(subset=['Sales', 'Profit', 'Region', 'Category'])

# 3. ANALYSIS 1: Top Product Categories by Sales
print("\n--- GENERATING CHART 1: CATEGORY SALES ---")
cat_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=cat_sales.values, y=cat_sales.index, palette='coolwarm')
plt.title('Top Categories by Total Sales')
plt.xlabel('Total Sales')
plt.ylabel('Category')
plt.tight_layout()

# Image-ah save pannidrom
plt.savefig('category_sales.png', dpi=300) 
plt.close() # Window open aagama close aiyidum
print("Chart 1 'category_sales.png' successfully saved!")

# 4. ANALYSIS 2: Regional Performance (Sales vs Profit)
print("\n--- GENERATING CHART 2: REGIONAL PERFORMANCE ---")
region_perf = df.groupby('Region')[['Sales', 'Profit']].sum()

# Reset index to make plotting with seaborn easier
region_perf_df = region_perf.reset_index()
# Melt data to side-by-side bar format
region_melted = pd.melt(region_perf_df, id_vars=['Region'], value_vars=['Sales', 'Profit'], 
                        var_name='Metric', value_name='Amount')

plt.figure(figsize=(10, 5))
sns.barplot(data=region_melted, x='Region', y='Amount', hue='Metric', palette='muted')
plt.title('Sales and Profit Performance by Region')
plt.xlabel('Region')
plt.ylabel('Amount')
plt.tight_layout()

# Image-ah save pannidrom
plt.savefig('regional_performance.png', dpi=300)
plt.close() # Window open aagama close aiyidum
print("Chart 2 'regional_performance.png' successfully saved!")

print("\nAll Analysis Charts Saved Successfully!")
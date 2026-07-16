import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("==================================================")
print("   TASK 2: TELCO CUSTOMER CHURN ANALYTICS       ")
print("==================================================")

# 1. Define the exact Kaggle dataset filename
file_name = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'

# Check if the file exists in the folder
if not os.path.exists(file_name):
    print(f"\n[ERROR] '{file_name}' not found in this folder!")
    print("Please make sure you dragged the extracted file into this directory.")
    exit()

print(f"\n[SUCCESS] Found dataset: '{file_name}'")
print("[Processing] Loading and cleaning data...")

# 2. Load dataset (Fixed: Removed the incorrect 'errors' parameter)
df = pd.read_csv(file_name, encoding='utf-8')
print(f"-> Successfully loaded {df.shape[0]} rows and {df.shape[1]} columns.")

# 3. Data Cleaning (Convert TotalCharges blank spaces to numeric values)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].astype(str).str.strip(), errors='coerce')
df = df.dropna(subset=['TotalCharges'])

# 4. Chart 1: Overall Churn Rate Distribution (Pie Chart)
print("\n[Processing] Generating Chart 1: Churn Breakdown...")
churn_counts = df['Churn'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(churn_counts, labels=['Retained (No)', 'Churned (Yes)'], autopct='%1.1f%%', 
        colors=['#2ecc71', '#e74c3c'], startangle=140, explode=(0, 0.05))
plt.title('Overall Customer Churn Rate Breakdown', fontsize=14, weight='bold')
plt.tight_layout()

# Save the chart directly into the folder
plt.savefig('churn_rate_distribution.png', dpi=300)
plt.close()
print("-> Chart 1 saved successfully as 'churn_rate_distribution.png'")

# 5. Chart 2: Churn by Contract Type (Countplot)
print("\n[Processing] Generating Chart 2: Churn Patterns by Contract Tiers...")
plt.figure(figsize=(9, 5))
sns.countplot(data=df, x='Contract', hue='Churn', palette='Set2')
plt.title('Customer Retention vs Churn by Contract Type', fontsize=14, weight='bold')
plt.xlabel('Contract Agreement Type', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.legend(title='Churn Status', labels=['Stayed (No)', 'Left (Yes)'])
plt.tight_layout()

# Save the chart directly into the folder
plt.savefig('churn_by_contract.png', dpi=300)
plt.close()
print("-> Chart 2 saved successfully as 'churn_by_contract.png'")

print("\n==================================================")
print("  CONGRATULATIONS HARINI! TASK 2 COMPLETED!       ")
print("==================================================")
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "nykaa_campaign_data.csv"

if not os.path.exists(file_name):
    print("Error: '" + file_name + "' not found in the current folder.")
else:
    df = pd.read_csv(file_name)
    print("Nykaa Dataset loaded successfully!")
    
    try:
        # Summing up the exact columns from your dataset
        metrics = {
            'Impressions': df['Impressions'].sum(),
            'Clicks': df['Clicks'].sum(),
            'Leads': df['Leads'].sum(),
            'Conversions': df['Conversions'].sum()
        }
        
        funnel_df = pd.DataFrame(list(metrics.items()), columns=['Stage', 'Count'])
        funnel_df['Conversion_Rate (%)'] = (funnel_df['Count'] / funnel_df['Count'].iloc[0]) * 100
        
        print("\n--- Marketing Funnel Analysis Table ---")
        print(funnel_df)

        plt.figure(figsize=(10, 6))
        sns.set_theme(style="whitegrid")
        
        # Added hue and legend=False to fix the FutureWarning
        ax = sns.barplot(x='Count', y='Stage', data=funnel_df, palette='flare', hue='Stage', legend=False)
        
        for i, value in enumerate(funnel_df['Count']):
            pct = funnel_df['Conversion_Rate (%)'].iloc[i]
            ax.text(value + (value * 0.01), i, f" {int(value):,} ({pct:.2f}%)", 
                    va='center', ha='left', fontsize=11, fontweight='bold', color='black')
            
        plt.title('Nykaa Marketing Funnel & Conversion Drop-off Analysis', fontsize=14, fontweight='bold', pad=20)
        plt.xlabel('Total Volume / Users', fontsize=12)
        plt.ylabel('Funnel Stage', fontsize=12)
        
        plt.xlim(0, funnel_df['Count'].max() * 1.25)
        plt.tight_layout()
        
        plt.savefig('marketing_funnel_analysis.png')
        print("\nSuccess! Funnel Chart saved as 'marketing_funnel_analysis.png'")
        plt.show()

    except Exception as e:
        print("An error occurred during analysis: " + str(e))
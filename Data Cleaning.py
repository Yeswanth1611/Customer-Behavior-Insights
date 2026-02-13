import pandas as pd
import os

#Defining path
file_path = r"C:\Users\yeswa\Downloads\Retail Customer Analysis\customer_shopping_behavior.csv"

#Checking existence of file
print("File exists:", os.path.exists(file_path))

#read csv file
df = pd.read_csv(file_path)

#checking any null values are present
print(df.isnull().sum())

#There are missing values in  review rating, so I am filling those missing items with median by category
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

print(df.head())

#checking any null values are present again
print(df.isnull().sum())

# Renaming columns according to snake casing for better readability and documentation
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

#Checking column names are valid
print(df.columns)

# create a new column age_group using Quantile-based cut
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)

print(df[['age','age_group']].head(10))

# create new column purchase_frequency_days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

print((df['discount_applied'] == df['promo_code_used']).all())

df = df.drop('promo_code_used', axis=1)

print(df.columns)

#Exporting to CSV
df.to_csv(r"C:\Users\yeswa\Downloads\Retail Customer Analysis\customerShoppingBehavior.csv", index=False)
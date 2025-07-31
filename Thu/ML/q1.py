import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

# Load dataset
df = pd.read_csv('startup_funding.csv', encoding='latin1')

# 1. Missing Values
missing_percent = df.isnull().mean() * 100
print("\nMissing Values Percentage:")
print(missing_percent)

# 2. Data Type Verification
print("\nData Types:")
print(df.dtypes)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 3. Standardize Date Format
invalid_dates = df['Date'].isna().sum()
print(f"\nInvalid/malformed dates: {invalid_dates}")

# 4. Duplicate Rows
duplicates = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")

# 5. Average Funding Amount
df['Amount in USD'] = pd.to_numeric(df['Amount in USD'], errors='coerce')
avg_funding = df['Amount in USD'].mean()
print(f"\nAverage funding amount: {avg_funding}")
funding_by_vertical = df.groupby('Industry Vertical')['Amount in USD'].mean().sort_values(ascending=False)

# 6. Bar Chart: Average Funding by Industry Vertical
funding_by_vertical.plot(kind='bar', figsize=(12,6))
plt.title('Average Funding Amount by Industry Vertical')
plt.ylabel('Average Amount in USD')
plt.tight_layout()
plt.show()

# Medium Questions

# 1. Outlier Detection (IQR)
Q1 = df['Amount in USD'].quantile(0.25)
Q3 = df['Amount in USD'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Amount in USD'] < Q1 - 1.5*IQR) | (df['Amount in USD'] > Q3 + 1.5*IQR)]
print(f"\nNumber of outliers: {outliers.shape[0]}")

# 2. Box Plot
df.boxplot(column='Amount in USD', figsize=(10,6))
plt.title('Outliers in Amount in USD')
plt.show()

# 3. Unique Industry Verticals
unique_verticals = df['Industry Vertical'].nunique()
print(f"\nUnique industry verticals: {unique_verticals}")

# 4. Investment Type Distribution
investment_dist = df['Investment Type'].value_counts()
print("\nInvestment Type Distribution:")
print(investment_dist)

# 5. Bar Chart: Investment Type
investment_dist.plot(kind='bar', figsize=(10,6))
plt.title('Distribution of Investment Types')
plt.ylabel('Number of Startups')
plt.show()

# 6. City with Highest Fundings
top_city = df['City Location'].value_counts().idxmax()
top_city_count = df['City Location'].value_counts().max()
print(f"\nTop city: {top_city}, Number of fundings: {top_city_count}")

# 7. Bar Chart: Startups per City
df['City Location'].value_counts().head(10).plot(kind='bar', figsize=(10,6))
plt.title('Top 10 Cities by Number of Startups')
plt.ylabel('Number of Fundings')
plt.show()

# 8. Funding Trends Over Years
df['Year'] = df['Date'].dt.year
funding_by_year = df.groupby('Year')['Amount in USD'].sum()
print("\nFunding by Year:")
print(funding_by_year)

# 9. Line Chart: Funding by Year
funding_by_year.plot(kind='line', marker='o')
plt.title('Total Funding Over Years')
plt.ylabel('Total Funding in USD')
plt.grid(True)
plt.show()

# Hard Questions

# 1. Correlation: Investment & Industry Vertical
filtered_df = df[['Industry Vertical', 'Amount in USD']].dropna()
groups = filtered_df.groupby('Industry Vertical')['Amount in USD'].apply(list)
f_stat, p_val = f_oneway(*groups)
print(f"\nANOVA F-statistic: {f_stat}, P-value: {p_val}")

# 2. Heatmap: Avg Funding by Industry Vertical
pivot = df.pivot_table(values='Amount in USD', index='Industry Vertical', aggfunc='mean')
plt.figure(figsize=(12,8))
sns.heatmap(pivot, cmap='YlGnBu', annot=True, fmt='.0f')
plt.title('Avg Funding by Industry Vertical')
plt.show()

# 3. Top Investor
top_investors = df.groupby('Investors Name')['Amount in USD'].sum().sort_values(ascending=False)
print("\nTop Investors:")
print(top_investors.head())

# 4. Bar Chart: Investment by Investor
top_investors.head(10).plot(kind='barh', figsize=(10,6))
plt.title('Top 10 Investors by Investment Amount')
plt.xlabel('Total Investment (USD)')
plt.gca().invert_yaxis()
plt.show()

# 5. Std Dev of Funding by Vertical
std_by_vertical = df.groupby('Industry Vertical')['Amount in USD'].std().sort_values(ascending=False)
print("\nStandard Deviation by Industry Vertical:")
print(std_by_vertical)

# 6. Bar Chart: Std Dev by Industry
std_by_vertical.plot(kind='bar', figsize=(12,6))
plt.title('Standard Deviation of Funding Amounts by Industry Vertical')
plt.ylabel('Standard Deviation')
plt.show()

# 7. Most Funded Industry
most_funded = df.groupby('Industry Vertical')['Amount in USD'].sum().sort_values(ascending=False)
print("\nMost Funded Industry:")
print(most_funded.head())

# 8. Bar Chart: Total Funding by Industry
most_funded.plot(kind='bar', figsize=(12,6))
plt.title('Total Funding Amount by Industry Vertical')
plt.ylabel('Total Amount in USD')
plt.show()

# 9. Comparative Analysis: City vs Industry
heatmap_data = df.pivot_table(values='Amount in USD', index='City Location', columns='Industry Vertical', aggfunc='sum')
plt.figure(figsize=(14,10))
sns.heatmap(heatmap_data, cmap='viridis', linewidths=0.5)
plt.title('Funding Amounts Across Cities and Industries')
plt.show()

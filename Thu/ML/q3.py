import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("indian_agriculture.csv")  # Adjust the file name accordingly

# EASY QUESTIONS

# 1. Crop Area Distribution: Rice, Wheat, Maize
crop_area = df[df['Crop'].isin(['Rice', 'Wheat', 'Maize'])]
total_area_by_crop = crop_area.groupby('Crop')['Area'].sum()
print("\nTotal area for Rice, Wheat, Maize:")
print(total_area_by_crop)

total_area_by_crop.plot(kind='bar', figsize=(8,6), color=['green', 'orange', 'yellow'])
plt.title("Total Area by Crop")
plt.ylabel("Area in 1000 ha")
plt.show()

# 2. Yearly Production for Rice
rice_data = df[df['Crop'] == 'Rice']
rice_by_year = rice_data.groupby('Year')['Production'].sum()
peak_year = rice_by_year.idxmax()
print(f"\nYear with highest rice production: {peak_year}")

plt.figure(figsize=(10,6))
plt.plot(rice_by_year.index, rice_by_year.values, marker='o')
plt.scatter(peak_year, rice_by_year[peak_year], color='red', label='Peak Year')
plt.title("Yearly Rice Production")
plt.xlabel("Year")
plt.ylabel("Production")
plt.legend()
plt.grid(True)
plt.show()

# 3. State Production for Wheat
wheat_data = df[df['Crop'] == 'Wheat']
wheat_by_state = wheat_data.groupby('State')['Production'].sum().sort_values()
print(f"\nState with lowest wheat production: {wheat_by_state.index[0]}")
print(f"State with highest wheat production: {wheat_by_state.index[-1]}")

wheat_by_state.plot(kind='barh', figsize=(10,10), color='goldenrod')
plt.title("Wheat Production by State")
plt.xlabel("Production")
plt.show()

# 4. Crop Yields for Sorghum
sorghum_data = df[df['Crop'] == 'Sorghum']
sorghum_data['Yield'] = sorghum_data['Production'] / sorghum_data['Area']
print("\nSorghum Yield Statistics:")
print(sorghum_data['Yield'].describe())

plt.figure(figsize=(8,6))
sns.boxplot(y=sorghum_data['Yield'], color='purple')
plt.title("Sorghum Yield Distribution")
plt.ylabel("Yield")
plt.show()

# 5. Vegetable Area by State
veg_data = df[df['Crop'].str.contains("Vegetable", case=False, na=False)]
total_veg_area = veg_data['Area'].sum()
veg_by_state = veg_data.groupby('State')['Area'].sum()
print(f"\nTotal vegetable area: {total_veg_area}")
max_veg_state = veg_by_state.idxmax()
print(f"State with maximum vegetable area: {max_veg_state}")

plt.figure(figsize=(10,8))
veg_by_state.plot(kind='pie', autopct='%1.1f%%')
plt.title("Vegetable Area Distribution by State")
plt.ylabel("")
plt.show()

# MEDIUM QUESTIONS

# 1. Area vs. Production Correlation (Chickpea)
chickpea_data = df[df['Crop'] == 'Chickpea']
correlation = chickpea_data[['Area', 'Production']].corr().loc['Area', 'Production']
print(f"\nCorrelation between Chickpea area and production: {correlation:.2f}")

plt.figure(figsize=(8,6))
sns.scatterplot(data=chickpea_data, x='Area', y='Production')
sns.regplot(data=chickpea_data, x='Area', y='Production', scatter=False, color='red')
plt.title("Chickpea Area vs Production")
plt.xlabel("Area")
plt.ylabel("Production")
plt.show()

# 2. Diversity of Crops per State
crop_diversity = df.groupby('State')['Crop'].nunique().sort_values(ascending=False)
print("\nNumber of different crops per state:")
print(crop_diversity)

plt.figure(figsize=(12,6))
crop_diversity.plot(kind='bar', color='skyblue')
plt.title("Crop Diversity by State")
plt.xlabel("State")
plt.ylabel("Number of Unique Crops")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
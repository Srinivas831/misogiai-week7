import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("swiggy.csv")  # Adjust filename as needed

# Easy Questions

# 1. Count Restaurants
restaurant_count = df.shape[0]
print(f"Total number of restaurants: {restaurant_count}")

# 2. Find Maximum Price
max_price = df['price'].max()
print(f"Highest restaurant price: {max_price}")

# 3. Average Ratings
avg_rating = df['rating'].mean()
print(f"Average rating: {avg_rating:.2f}")

# 4. Total Ratings
total_ratings = df['rating_count'].sum()
print(f"Total number of ratings: {total_ratings}")

# 5. Food Type Count
food_type_count = df['food_type'].nunique()
print(f"Number of unique food types: {food_type_count}")

# Medium Questions

# 1. Top Cities by Restaurant Count
top_cities = df['city'].value_counts().head(3)
print("\nTop 3 cities by number of restaurants:")
print(top_cities)

# 2. Average Price by Food Type
avg_price_by_food = df.groupby('food_type')['price'].mean().sort_values(ascending=False)
print("\nAverage price by food type:")
print(avg_price_by_food)

# 3. Bar Chart: Average Price by Food Type
avg_price_by_food.plot(kind='bar', figsize=(10,6))
plt.title("Average Price by Food Type")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Histogram: Rating Distribution
df['rating'].hist(bins=20, figsize=(10,6))
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.show()

# 5. Average Delivery Time (Rating > 4)
avg_delivery_high_rating = df[df['rating'] > 4]['delivery_time'].mean()
print(f"\nAverage delivery time for restaurants with rating > 4: {avg_delivery_high_rating:.2f} mins")

# 6. Top 5 Rated Restaurants
top_5_restaurants = df.sort_values(by='rating', ascending=False).head(5)[['name', 'rating', 'food_type']]
print("\nTop 5 restaurants by rating:")
print(top_5_restaurants)

# Hard Questions

# 1. Correlation: Price vs Rating
correlation = df[['price', 'rating']].corr().loc['price', 'rating']
print(f"\nCorrelation coefficient between price and rating: {correlation:.2f}")

# Scatter Plot
sns.scatterplot(data=df, x='price', y='rating')
plt.title("Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Rating")
plt.show()

# 2. Delivery Time Outliers Box Plot
plt.figure(figsize=(8,6))
sns.boxplot(x=df['delivery_time'])
plt.title("Delivery Time Outliers")
plt.xlabel("Delivery Time (minutes)")
plt.show()

# 3. Price vs Rating Category Box Plot
def rating_category(r):
    if r < 3:
        return "Below 3"
    elif 3 <= r <= 4:
        return "3-4"
    else:
        return "Above 4"

df['rating_category'] = df['rating'].apply(rating_category)
sns.boxplot(data=df, x='rating_category', y='price')
plt.title("Price Distribution by Rating Category")
plt.xlabel("Rating Category")
plt.ylabel("Price")
plt.show()

# 4. Grouped Analysis: Avg Price and Rating per City
city_group = df.groupby('city')[['price', 'rating']].mean().sort_values(by='price', ascending=False).head(10)
print("\nAverage price and rating per city:")
print(city_group)

# Grouped Bar Chart
city_group.plot(kind='bar', figsize=(12,6))
plt.title("Average Price and Rating by City")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

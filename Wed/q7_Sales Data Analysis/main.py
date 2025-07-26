sales_data = [
    ("Q1", [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)]),
    ("Q2", [("Apr", 1300), ("May", 1250), ("Jun", 1400)]),
    ("Q3", [("Jul", 1350), ("Aug", 1450), ("Sep", 1300)])
]


for i in sales_data:
    total=0
    for j in i[1]:
        total=total+j[1]
    print(f"{i[0]}", total)

for quarter, monthly_sales in sales_data:
    total = sum(sale for month, sale in monthly_sales)
    print(f"{quarter}: {total}")


# Identify the month with the highest individual sales across all quarters.


max = float("-inf")
month = None
for q in sales_data:
    for k in q[1]:
        if k[1] > max:
            max = k[1]
            month = k[0]
print(max)
print(month)


arr = list()
for i in sales_data:
    arr.extend(i[1])
print(arr)


# Use tuple unpacking while iterating to clearly separate months, sales values, and quarters.

for quarter, month_data in sales_data:
    print(f"\n{quarter} sales breakdown:")
    for month, sales in month_data:
        print(f"  {month}: {sales}")

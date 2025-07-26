products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 25.50, 75.00, 299.99]
quantities = [5, 20, 15, 8]

product_price_pairs = list(zip(products, prices))
# print(product_price_pairs)

# Calculate Total Value for Each Product

# for i in products:
#     total = prices*quantities
# print("total", total)

for product, price, quantity in zip(products, prices, quantities):
    total = price * quantity
print(total)


catalog = dict()
import json
for product, price, quantity in zip(products, prices, quantities):
    catalog[product] = {
        "price":price,
        "quantity":quantity
    }
print(json.dumps(catalog, indent=4))

for key in catalog:
    if catalog[key]["quantity"]<10:
        print("fds",key)




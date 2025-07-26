import json

inventory = {
    "apples": {"price": 1.50, "quantity": 100},
    "bananas": {"price": 0.75, "quantity": 150},
    "oranges": {"price": 2.00, "quantity": 80}
}


# add a new product
inventory["pineapple"]={"price":2.5, "quantity":120}

inventory["apples"]["price"] = 3.00


# inventory["apples"]= {"quantity"}
if inventory["apples"]["price"] >= 25:
    inventory["apples"]["price"]-=25
else:
    print("Not enough apples in stock!")


# Calculate Total Inventory Value
# Compute the total value of the inventory using the formula:
# total = sum(price × quantity for all products)
total=0
for i in inventory:
    # print(i)
    total = (inventory[i]["quantity"]*inventory[i]["price"])
print(total)


# Find Low Stock Products
for i in inventory:
    if inventory[i]["quantity"]<100:
        # print(inventory[i])
        print(f"- {i}: {inventory[i]['quantity']} units")

# print(json.dumps(inventory, indent=4))
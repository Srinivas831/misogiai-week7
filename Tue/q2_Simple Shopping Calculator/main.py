item1 = float(input("Enter the price of the first item: "))
quantity1 = int(input("Enter the quantity of the first item: "))
item2 = float(input("Enter the price of the second item: "))
quantity2 = int(input("Enter the quantity of the second item: "))
item3 = float(input("Enter the price of the third item: "))
quantity3 = int(input("Enter the quantity of the third item: ")) 

total_before_tax = (item1 * quantity1) + (item2 * quantity2) + (item3 * quantity3)
total_after_tax = total_before_tax + (total_before_tax * (8.5/100))

print(f"The total cost of the items after tax is {total_after_tax:.2f}")



fruits_list = ['apple', 'banana', 'orange', 'apple', 'grape']
fruits_tuple = ('apple', 'banana', 'orange')
fruits_set = {'apple', 'banana', 'orange', 'grape'}
fruits_dict = {'apple': 5, 'banana': 3, 'orange': 8, 'grape': 2}


print("apple" in fruits_list)   # True
print("apple" in fruits_tuple)  # True
print("apple" in fruits_set)    # True
print("apple" in fruits_dict)   # True (checks keys)


print(len(fruits_list))   # 5 (includes duplicates)
print(len(fruits_tuple))  # 3
print(len(fruits_set))    # 4 (duplicates removed)
print(len(fruits_dict))   # 4 (number of keys)



print("List:")
for fruit in fruits_list:
    print(fruit)

print("\nTuple:")
for fruit in fruits_tuple:
    print(fruit)

print("\nSet:")
for fruit in fruits_set:
    print(fruit)

print("\nDict (key → value):")
for key in fruits_dict:
    print(f"{key} → {fruits_dict[key]}")

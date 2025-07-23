# fstrings
name = "Alice"
age = 10
city = "Delhi"

print(f"My name is {name} and i am {age} years old. I live in {city}.")

# %formatting
print("My name is %s and i am %d years old. I live in %s." %(name, age, city))

# .format()
print("My name is {name} and i am {age} years old. I live in {city}.".format(name=name, age=age, city=city))
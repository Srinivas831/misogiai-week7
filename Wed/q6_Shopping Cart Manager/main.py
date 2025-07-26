cart = list()

def add_item(item):
    cart.append(item)
    print(f"{item} is added")

add_item("banana")
add_item("pineapple")
add_item("Apple")

# print(cart)


# cart.remove("banana")
# print(cart)

# cart.pop()

sortedd = sorted(cart)
print(sortedd)


for ind, i in enumerate(cart):
    print(f"{ind}:{i}")
  


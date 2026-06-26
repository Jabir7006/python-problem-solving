cart = [
    {"item": "T-shirt", "price": 500},
    {"item": "Jeans", "price": 1200},
    {"item": "Shoes", "price": 2500}
]

total = 0

for item in cart:
    total += item['price']

print(total) 
duplicate_products = ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Monitor"]

clean_products = []


for item in duplicate_products:
    if item not in clean_products:
        clean_products.append(item)

print(clean_products)
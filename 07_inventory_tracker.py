sales_items = ["Apple", "Banana", "Apple", "Orange", "Apple", "Mango", "Banana"]

# first way
count = 0

for item in sales_items:
    if item == 'Apple':
        count += 1
print(count)


# second way (short and easy method)
count2 = sales_items.count('Apple')
print(count2)
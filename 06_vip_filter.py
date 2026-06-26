all_guests = ["Rahim", "Karim", "Zayan", "Jabir", "Fahim"]

for guest in all_guests:
    if guest == 'Zayan' or guest == 'Jabir':
        print(f'{guest} is a VIP guest!')
    else:
        print(f'{guest} is a Regular guest!')

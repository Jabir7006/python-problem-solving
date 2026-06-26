guests = []

while True:
    guest_name = input("Please enter guest name: ")

    if guest_name == 'stop':
        break

    guests.append(guest_name)
    print(f'{guest_name} added to the guest list!')

print(guests)
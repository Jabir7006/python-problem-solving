while True:
    total_amount = int(input("Please enter total amount: "))

    if total_amount == 0:
        break
    elif total_amount >= 1000:
        print("You get a 10% discount!")
    else:
        print("Thank you for shopping!")
        
    
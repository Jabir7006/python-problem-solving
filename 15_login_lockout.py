def bank_login():
    for i in range(3):
        password = input('Please enter you password: ')
        
        if password == 'Secure123':
            print('Login Successful!')
            break
    else:
        print('Account Locked due to multiple failed attempts!') 

bank_login()

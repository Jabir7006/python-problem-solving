def is_valid_username(username):
    if len(username) < 5:
        return False
    elif ' ' in username:
        return False
    else:
        return True


print(is_valid_username('jabir_ahmad'))
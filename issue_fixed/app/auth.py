from .database import find_user

def authenticate(username, password):
    user = find_user(username)
    if not user:
        return False
    return user[2] == password
# ❌ INSECURE: plaintext password storage

database = {}

def create_user(username, password):
    database[username] = password

def authenticate_user(username, password):
    if username not in database:
        return False
    return database[username] == password

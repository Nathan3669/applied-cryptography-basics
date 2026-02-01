import bcrypt

# Simulated database
database = {}

def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def create_user(username: str, password: str):
    password_hash = hash_password(password)
    database[username] = password_hash

def authenticate_user(username: str, password: str) -> bool:
    if username not in database:
        return False
    return bcrypt.checkpw(password.encode(), database[username])

import os
from cryptography.fernet import Fernet

def load_key() -> bytes:
    """
    Load encryption key from environment variable.
    In real systems, keys must never be hardcoded.
    """
    key = os.getenv("APP_ENCRYPTION_KEY")
    if not key:
        raise RuntimeError("Encryption key not set")
    return key.encode()

def encrypt_data(data: str) -> bytes:
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(token: bytes) -> str:
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(token).decode()

# ❌ INSECURE: no real encryption, reversible transformation

def encrypt_data(data: str) -> str:
    return data[::-1]

def decrypt_data(data: str) -> str:
    return data[::-1]

# Secure Password Hashing

## Real-World Problem
Applications often store user passwords insecurely, exposing credentials if the database is leaked.

## Insecure Pattern
Passwords are stored and compared in plaintext.

## Secure Pattern
Passwords are hashed using a strong adaptive hashing algorithm before storage.

## Why bcrypt?
- Built-in salting
- Resistant to brute-force attacks
- Widely used in production systems

## Key Takeaway
Passwords must never be stored or transmitted in plaintext.

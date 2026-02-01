# Secure Data Encryption

## Real-World Scenario
Sensitive data such as tokens or personal information must be protected at rest.

## Insecure Pattern
Custom or reversible encryption mechanisms.

## Secure Pattern
Symmetric encryption using a trusted cryptographic library.

## Key Management
- Encryption keys are loaded from environment variables
- Keys should be rotated and protected

## Key Takeaway
Never implement custom encryption. Use vetted libraries and manage keys securely.

import hashlib

# Store the SHA-256 hash of the password: Summer@2026
stored_hash = hashlib.sha256("Summer@2026".encode()).hexdigest()

# Prompt the user for a password
password = input("Enter password: ")

# Hash the entered password
entered_hash = hashlib.sha256(password.encode()).hexdigest()

# Compare hashes
if entered_hash == stored_hash:
    print("Authentication Successful")
else:
    print("Authentication Failed")
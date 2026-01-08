import hashlib
import secrets

# For secure password hashing, combine the password with a unique salt
password = b"mySecurePassword123"
salt = secrets.token_bytes(16) # Use the secrets module for a cryptographically strong salt

# Hash the password and salt using SHA256
hashed_password = hashlib.sha256(salt + password).hexdigest()
print(f"Hashed password with salt: {hashed_password}")

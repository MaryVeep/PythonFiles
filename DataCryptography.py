from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet cipher (store the key securely in a real application)
key = Fernet.generate_key()
f = Fernet(key)

# Encrypt a message
message = b"This is sensitive data."
encrypted_message = f.encrypt(message)
print(f"Encrypted: {encrypted_message}")

# Decrypt the message
decrypted_message = f.decrypt(encrypted_message).decode()
print(f"Decrypted: {decrypted_message}")

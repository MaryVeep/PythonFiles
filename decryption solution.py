# adapted from https://devqa.io/encrypt-decrypt-data-python/

from cryptography.fernet import Fernet
keyFile = open("secret.key", "r")
key = open("secret.key").read()
keyFile.close()
print(key)
fernet = Fernet(key)
encryptedMessage = open("Encrypted tic tac toe.txt", "r").read().encode()
decryptedMessage = fernet.decrypt(encryptedMessage).decode()
decryptedFile = open("Decrypted tic tac toe.py", "w")
decryptedFile.write(decryptedMessage)
decryptedFile.close()

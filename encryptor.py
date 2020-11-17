# encrypts files with a given secret.key file

from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# f = open("secret.key", "wb")
# f.write(key)
# f.close()
key = open("secret.key").readline()
print(key)

ticFile = open("Tic tac toe.py", "r")
ticString = ticFile.read()
ticFile.close()
print(ticString)
f = Fernet(key)
encString = f.encrypt(ticString.encode())
print(encString)
encFile = open("Encrypted tic tac toe.txt", "w")
encFile.write(encString.decode())
encFile.close()

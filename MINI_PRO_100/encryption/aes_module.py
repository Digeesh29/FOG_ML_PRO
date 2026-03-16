from cryptography.fernet import Fernet

def aes_encrypt(data):

    key = Fernet.generate_key()

    cipher = Fernet(key)

    encrypted = cipher.encrypt(data.encode())

    return encrypted, key


def aes_decrypt(ciphertext, key):

    cipher = Fernet(key)

    return cipher.decrypt(ciphertext).decode()
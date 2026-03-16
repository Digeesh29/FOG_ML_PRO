from encryption.aes_module import aes_encrypt
from encryption.ecc_module import generate_ecc_keys

def hybrid_encrypt(data):

    encrypted_data, aes_key = aes_encrypt(data)

    private_key, public_key = generate_ecc_keys()

    return encrypted_data, aes_key, public_key
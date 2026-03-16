from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def generate_ecc_keys():

    private_key = ec.generate_private_key(ec.SECP256R1())

    public_key = private_key.public_key()

    return private_key, public_key
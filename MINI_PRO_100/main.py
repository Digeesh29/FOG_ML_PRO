import pandas as pd
from models.predict import classify_data
from encryption.aes_module import aes_encrypt
from encryption.hybrid_encryption import hybrid_encrypt
from fog_node.fog_storage import store_in_fog
import socket
from performance import measure_encryption_time

sample_data = pd.DataFrame(
    [[1,250,0,2]],
    columns=[
        "file_type",
        "file_size_kb",
        "owner_type",
        "data_category"
    ]
)

prediction = classify_data(sample_data)

print("Prediction:", prediction)

data_string = sample_data.to_string()

if prediction == 1:

    print("Sensitive Data → Hybrid Encryption")

    encrypted, key, pub = measure_encryption_time(hybrid_encrypt, data_string)

else:

    print("Normal Data → AES Encryption")

    encrypted, key = measure_encryption_time(aes_encrypt, data_string)

def send_to_fog(data):

    HOST = '127.0.0.1'
    PORT = 5001

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client.sendall(data)

    client.close()

send_to_fog(encrypted)
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def store_in_fog(data):

    folder = "fog_node/stored_data/"

    if not os.path.exists(folder):
        os.makedirs(folder)

    path = folder + "encrypt_data.bin"

    with open(path, "wb") as f:
        f.write(data)

    print("Stored in Fog:", path)
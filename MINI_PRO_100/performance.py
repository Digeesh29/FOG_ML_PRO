import time

def measure_encryption_time(func, data):

    start = time.time()

    result = func(data)

    end = time.time()

    print("Encryption Time:", end - start)

    return result
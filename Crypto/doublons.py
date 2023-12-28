import math
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

def read_keys(file_path):
    with open(file_path, 'r') as file:
        key_strings = file.read().strip().split('\n\n')
    keys = []
    for key_str in key_strings:
        try:
            key = load_pem_public_key(key_str.encode(), default_backend())
            if isinstance(key.public_numbers(), rsa.RSAPublicNumbers):
                modulus = key.public_numbers().n
                keys.append((modulus, key_str))
        except:
            continue
    return keys

def batch_gcd(keys):
    n = len(keys)
    gcds = [0] * n
    prod = 1
    for i in range(n):
        prod *= keys[i][0]
    for i in range(n):
        mod = keys[i][0]
        gcds[i] = math.gcd(prod // mod, mod)
    return gcds

def find_common_factors(keys, gcds):
    common_factors = []
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            if gcds[i] == gcds[j] and gcds[i] != 1:
                common_factors.append((keys[i][1], keys[j][1]))
    return common_factors

def process(input_file, output_file):
    keys = read_keys(input_file)
    gcds = batch_gcd(keys)
    compromised_keys = find_common_factors(keys, gcds)

    with open(output_file, 'w') as file:
        for key_pair in compromised_keys:
            file.write(f"{{ {key_pair[0]}, {key_pair[1]} }}\n\n\n")


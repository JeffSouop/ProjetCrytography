from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Clé publique au format PEM
public_key_pem = """
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEGNCINYcF2Xw7ElV1Wth4z/bfRRwL
Erao5GZLjH004tuzIBpzCgKmeMVNv+V34RzW9+LpHR10eozIDY8HeJXyfg==
-----END PUBLIC KEY-----
"""

# Charger la clé publique PEM
public_key = serialization.load_pem_public_key(
    public_key_pem.encode(),  # Convertir en bytes
)

# Extraire le module (n) et l'exposant public (e)
n = public_key.public_numbers().n
e = public_key.public_numbers().e

print(f"Module (n): {n}")
print(f"Exposant public (e): {e}")

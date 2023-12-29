from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from math import gcd

def calculate_gcd(key1, key2):
    # Charger les clés publiques
    public_key1 = serialization.load_pem_public_key(key1.encode())
    public_key2 = serialization.load_pem_public_key(key2.encode())

    # Récupérer les nombres de modules des clés publiques
    modulus1 = public_key1.public_numbers().n
    modulus2 = public_key2.public_numbers().n

    # Calculer le PGCD des modules
    return gcd(modulus1, modulus2)

# Deux clés publiques (format PEM)
key1 = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzBhTgGw2olB2x8ebKNYA
mjq7aIK984r9vfUu5jXrVBNVO0xG+Tc94H71iHRaftd+RzkKrsLH7tQrIuO9B7MT
an8w9eVNTWrs8qBQEERMOhnMy8Jz8gQA6/ebIv5Zvqq8MPaNzPviLiv48gT3jBoP
5RNHoswyzyYAbTO1IE5oKyfbKSHrjyfO4OEfudof3GMzQa3mN4aWEzsp3IhC2gvA
JyQ/FgMOy7n6zm4DGHpOUY4/KT7hOIYcnxqyTPTxjYkHx95kwmKS0901wCYEVIlM
uYGvzieDzY8rBKxSbpOsndGpQK44R24iKgrCSCjOBpcNOFdLCg3078yQRNbWKw8X
eQIDAQAZ
-----END PUBLIC KEY-----
"""

key2 = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzBhTgGw2olB2x8ebKNYA
mjq7aIK984r9vfUu5jXrVBNVO0xG+Tc94H71iHRaftd+RzkKrsLH7tQrIuO9B7MT
an8w9eVNTWrs8qBQEERMOhnMy8Jz8gQA6/ebIv5Zvqq8MPaNzPviLiv48gT3jBoP
5RNHoswyzyYAbTO1IE5oKyfbKSHrjyfO4OEfudof3GMzQa3mN4aWEzsp3IhC2gvA
JyQ/FgMOy7n6zm4DGHpOUY4/KT7hOIYcnxqyTPTxjYkHx95kwmKS0901wCYEVIlM
uYGvzieDzY8rBKxSbpOsndGpQK44R24iKgrCSCjOBpcNOFdLCg3078yQRNbWKw8X
uQIDAQAB
-----END PUBLIC KEY-----
"""

result = calculate_gcd(key1, key2)
print("Le PGCD des modules des clés publiques est :", result)

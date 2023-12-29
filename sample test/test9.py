from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def extract_modulus(public_key):
    try:
        # Charger la clé publique au format PEM
        pem_data = public_key.encode()
        loaded_key = serialization.load_pem_public_key(pem_data)

        # Obtenir les paramètres de la clé publique
        public_numbers = loaded_key.public_numbers()

        # Extraire le module (n) de la clé publique
        modulus = public_numbers.n
        return modulus
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None

# Exemple d'utilisation
public_key_str = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzBhTgGw2olB2x8ebKNYd
mjq7aIK984r9vfUu5jXrVBNVO0xG+Tc94H71iHRaftd+RzkKrsLH7tQrIuO9B7MY
an8w9eVNTWrs8qBQEERMOhnMy8Jz8gQA6/ebIv5Zvqq8MPaNzPviLiv48gT3jBoe
5RNHoswyzyYAbTO1IE5oKyfbKSHrd76O4OEfudof3GMzQa3mN4aWEzsp3IhC2gvT
JyQ/FgMOy7n6zm4DGHpOUY4/KT7hOIYcnxqyTPTxjYkHx95kwmKS0901wCYEVIlJ
uYGvzieDzY8rSKxSbpOsndGpQK44R24iKgrCSCjOBpcNOFdLCg3078yQRNbWKw8W
uQIDAQAB
-----END PUBLIC KEY-----
"""

modulus = extract_modulus(public_key_str)
if modulus is not None:
    print("Module (n) de la clé publique:", modulus)
else:
    print("Échec de l'extraction du module de la clé publique.")

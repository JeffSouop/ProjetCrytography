def convert_to_single_line(public_key):
    return public_key.replace("\n", "")

# Clé multi-lignes
multi_line_key = """
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

# Conversion en une seule ligne sans les entêtes et pieds de page
single_line_key = convert_to_single_line(multi_line_key)
print(single_line_key)

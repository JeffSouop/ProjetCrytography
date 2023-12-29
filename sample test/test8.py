def format_key(key):
    header = "-----BEGIN PUBLIC KEY-----\n"
    footer = "\n-----END PUBLIC KEY-----"
    formatted_key = header + "\n".join([key[i:i+64] for i in range(0, len(key), 64)]) + footer
    return formatted_key

# Exemple de clé en ligne
key_in_one_line = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzBhTgGw2olB2x8ebKNYdmjq7aIK984r9vfUu5jXrVBNVO0xG+Tc94H71iHRaftd+RzkKrsLH7tQrIuO9B7MYan8w9eVNTWrs8qBQEERMOhnMy8Jz8gQA6/ebIv5Zvqq8MPaNzPviLiv48gT3jBoe5RNHoswyzyYAbTO1IE5oKyfbKSHrd76O4OEfudof3GMzQa3mN4aWEzsp3IhC2gvTJyQ/FgMOy7n6zm4DGHpOUY4/KT7hOIYcnxqyTPTxjYkHx95kwmKS0901wCYEVIlJuYGvzieDzY8rSKxSbpOsndGpQK44R24iKgrCSCjOBpcNOFdLCg3078yQRNbWKw8WuQIDAQAB"

formatted_key = format_key(key_in_one_line)
print(formatted_key)

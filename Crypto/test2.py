# Nom du fichier contenant les certificats au format PEM
fichier_certificats = 'certificat.txt'

# Compteur pour le nombre de certificats
nombre_certificats = 0

# Ouvrir le fichier contenant les certificats
with open(fichier_certificats, 'r') as f:
    cert_pem = ''
    for line in f:
        if '-----END CERTIFICATE-----' in line:
            nombre_certificats += 1
            cert_pem = ''

print(f"Le fichier {fichier_certificats} contient {nombre_certificats} certificats.")

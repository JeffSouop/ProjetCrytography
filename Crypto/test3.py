import csv
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

fichier_certificats = 'certificat.txt'
cert_pems = []

# Lire les certificats
with open(fichier_certificats, 'r') as f:
    current_cert = ''
    for line in f:
        current_cert += line
        if '-----END CERTIFICATE-----' in line:
            cert_pems.append(current_cert.strip())
            current_cert = ''

# Extraction des informations
rows = []
for cert_pem in cert_pems:
    cert = x509.load_pem_x509_certificate(cert_pem.encode(), default_backend())

    common_name = None
    for attr in cert.subject:
        if attr.oid == x509.NameOID.COMMON_NAME:
            common_name = attr.value
            break

    public_key = cert.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    rows.append({
        "certificat": cert_pem,
        "cle_publique": public_key.decode(),
        "CN": common_name
    })

# Écrire dans un fichier CSV
csv_columns = ["certificat", "cle_publique", "CN"]
csv_file = "informations_certificats.csv"

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

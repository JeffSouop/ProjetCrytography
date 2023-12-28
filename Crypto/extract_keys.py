from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


"""def process_certificates(input_file, output_file):
    with open(input_file, 'r') as cert_file:
        certificates = cert_file.read().split('\n\n')

    with open(output_file, 'w') as keys_file:
        for cert_data in certificates:
            try:
                cert = x509.load_pem_x509_certificate(cert_data.encode(), default_backend())
                public_key = cert.public_key()
                pem_public_key = public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ).decode('utf-8')
                keys_file.write(pem_public_key + '\n')
            except Exception as e:
                print(f"Error processing certificate: {str(e)}")"""


from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def process_certificates(input_file, output_file):
    with open(input_file, 'r') as cert_file:
        certificates = cert_file.read().split('\n\n')

    keys_dict = {}  # Dictionnaire pour stocker les clés

    for cert_data in certificates:
        try:
            cert = x509.load_pem_x509_certificate(cert_data.encode(), default_backend())
            public_key = cert.public_key()
            pem_public_key = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode('utf-8')
            key_length = len(pem_public_key)  # Longueur de la clé comme clé de tri
            if key_length not in keys_dict:
                keys_dict[key_length] = []  # Initialisation pour chaque longueur de clé
            keys_dict[key_length].append(pem_public_key)
        except Exception as e:
            print(f"Error processing certificate: {str(e)}")

    # Écriture triée des clés dans le fichier de sortie
    with open(output_file, 'w') as keys_file:
        for length in sorted(keys_dict.keys()):  # Parcours des longueurs triées
            for key in keys_dict[length]:
                keys_file.write(key + '\n')

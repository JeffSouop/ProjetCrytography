from cryptography import x509
from cryptography.hazmat.backends import default_backend
import base64

# Fonction pour extraire les certificats PEM d'un fichier texte
def extract_certificates_from_file(file_path):
    certificates = []
    
    with open(file_path, 'r') as file:
        data = file.read()
        # Sépare les certificats par les délimiteurs PEM
        pem_certificates = data.split('-----END CERTIFICATE-----')
        
        for pem_certificate in pem_certificates:
            # Reconstitue le certificat en ajoutant les délimiteurs
            pem_certificate = pem_certificate.strip() + '\n-----END CERTIFICATE-----\n'
            certificates.append(pem_certificate)
    
    return certificates


def extract_domain_names(cert_str):
    # Conversion du certificat en format DER pour l'analyser
    cert = x509.load_der_x509_certificate(cert_str, default_backend())

    # Extraire le Common Name
    common_name = cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
    print(f"{common_name}")

    # Vérifier et extraire les Subject Alternative Names, s'ils existent
    try:
        san = cert.extensions.get_extension_for_oid(x509.ExtensionOID.SUBJECT_ALTERNATIVE_NAME).value
        # print("Subject Alternative Names:")
        for name in san:
            pass
            # print(name)
    except x509.ExtensionNotFound:
        pass
        # print("No Subject Alternative Name extension found in the certificate.")

# Fonction pour afficher les certificats
def print_certificates(certificates):
    for i, cert in enumerate(certificates, start=1):
        print(cert)
        print("\n")

def main():
    input_file = "certificat.txt"  # Remplacez par le chemin de votre fichier

    # Extrait les certificats du fichier
    certificates = extract_certificates_from_file(input_file)

    # Affiche les certificats
    # print_certificates(certificates)
    cn = extract_domain_names(certificates)
    print(cn)


if __name__ == "__main__":
     main()

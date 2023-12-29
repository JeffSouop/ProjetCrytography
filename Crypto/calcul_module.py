import csv
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

class CertificateProcessor:
    def __init__(self, certificates_file, output_csv_file):
        self.certificates_file = certificates_file
        self.output_csv_file = output_csv_file

    def calculate_module(self, public_key):
        try:
            decoded_public_key = public_key.encode()
            key = serialization.load_pem_public_key(decoded_public_key, backend=default_backend())
            modulus = key.public_numbers().n
            return modulus
        except Exception as e:
            print(f"Error calculating modulus: {e}")
            return None

    def read_certificates(self):
        cert_pems = []
        with open(self.certificates_file, 'r') as f:
            current_cert = ''
            for line in f:
                current_cert += line
                if '-----END CERTIFICATE-----' in line:
                    cert_pems.append(current_cert.strip())
                    current_cert = ''
        return cert_pems

    def extract_information(self, cert_pems):
        rows = []
        for cert_pem in cert_pems:
            cert = x509.load_pem_x509_certificate(cert_pem.encode(), default_backend())

            common_name = None
            for attr in cert.subject:
                if attr.oid == x509.NameOID.COMMON_NAME:
                    common_name = attr.value
                    break

            organization_name = None
            for attr in cert.issuer:
                if attr.oid == x509.NameOID.ORGANIZATION_NAME:
                    organization_name = attr.value
                    break

            public_key = cert.public_key().public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

            rows.append({
                "certificat": cert_pem,
                "cle_publique": public_key.decode(),
                "CN": common_name,
                "Organization": organization_name
            })
        return rows

    def update_information_with_modules(self, rows):
        for row in rows:
            public_key = row["cle_publique"]
            modulus = self.calculate_module(public_key)
            row["module"] = modulus
        return rows

    def write_to_csv(self, rows):
        csv_columns = ["certificat", "cle_publique", "CN", "Organization", "module"]
        with open(self.output_csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

    def process_certificates(self):
        cert_pems = self.read_certificates()
        rows = self.extract_information(cert_pems)
        rows = self.update_information_with_modules(rows)
        self.write_to_csv(rows)


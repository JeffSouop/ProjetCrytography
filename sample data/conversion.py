from cryptography import x509
from cryptography.hazmat.backends import default_backend
from crawler import Crawler
from certificate import Certificate
from key_analyzer import KeyAnalyzer
from BatchGCD import BatchGCD
from cryptography.hazmat.primitives import serialization


class Conversion:
    def read_links_from_file(self, file_path):
        """
        Lit les liens depuis un fichier texte et retourne une liste d'URLs.
        """
        with open(file_path, 'r') as file:
            links = file.read().splitlines()
        return links

    def save_keys_to_file(self, file_path, keys):
        """
        Enregistre les clés dans un fichier texte au format PEM.
        """
        with open(file_path, 'w') as file:
            for key in keys:
                pem_key = key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
                file.write(pem_key.decode('utf-8') + '\n')

    def save_certificates_to_file(self, file_path, certificates):
        """
        Enregistre les certificats dans un fichier texte.
        """
        with open(file_path, 'w') as file:
            for cert in certificates:
                # file.write(str(cert)+'\n')
                pem_cert = cert.public_bytes(encoding=serialization.Encoding.PEM)
                file.write(str(pem_cert.decode('utf-8')) + '\n')

    def process_certificates_and_find_common_factors(self, links_file_path):
        urls = self.read_links_from_file(links_file_path)

        if not urls:
            print("Aucun lien trouvé dans le fichier.")
            return

        # Crée une instance du Crawler pour télécharger les certificats
        crawler = Crawler(urls)
        certificates = crawler.download_certificates()

        if certificates:
            key_analyzer = KeyAnalyzer(certificates)

            output_file = "certif.txt"

            self.save_certificates_to_file(output_file, certificates)
            print(f"Les certificats ont été enregistrés dans {output_file}")

            batch_gcd = BatchGCD(certificates)
            common_factors_batch = BatchGCD.find_common_factors(certificates)

            # Chemin vers le fichier texte pour enregistrer les clés similaires
            output_file_path = "similar_certificate.txt"

            if common_factors_batch:
                self.save_keys_to_file(output_file_path, common_factors_batch)
                print(f"Les clés similaires ont été enregistrées dans {output_file_path}")
            else:
                print("\nAucune paire de clés avec des facteurs communs trouvée.")
        else:
            print("Aucun certificat téléchargé depuis les URLs fournies.")

    def run(self):
        links_file_path = "links.txt"
        self.process_certificates_and_find_common_factors(links_file_path)




    """def extract_public_keys_from_certificates(self, certificates_file_path):
        """"""
        Extrait les clés publiques des certificats dans le fichier spécifié.
        """"""
        with open(certificates_file_path, 'r') as file:
            certificate_contents = file.read()

        pem_certificates = certificate_contents.split('-----BEGIN CERTIFICATE-----')

        public_keys = []
        for pem_cert in pem_certificates:
            if pem_cert.strip():
                pem_cert = '-----BEGIN CERTIFICATE-----' + pem_cert
                cert = x509.load_pem_x509_certificate(pem_cert.encode('utf-8'), default_backend())
                public_key = cert.public_key()
                pem_public_key = public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
                public_keys.append(pem_public_key.decode('utf-8'))

        with open('keys.txt', 'w') as file:
            for key in public_keys:
                file.write(key + '\n')"""

import requests
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

class Crawler:
    def __init__(self, urls):
        """
        Initialise le Crawler avec une liste d'URLs.
        :param urls: Liste des URLs des certificats à télécharger.
        """
        self.urls = urls

    def download_certificates(self):
        certificates = []
        for url in self.urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    # Vérifier si le contenu est du texte (PEM) ou binaire (DER)
                    if "-----BEGIN CERTIFICATE-----" in response.text:
                        # Traiter chaque certificat PEM dans le contenu
                        pem_certificates = response.content.decode().split("-----END CERTIFICATE-----")
                        for pem in pem_certificates:
                            if pem.strip():
                                pem = f"{pem}-----END CERTIFICATE-----\n"
                                try:
                                    cert = x509.load_pem_x509_certificate(pem.encode(), default_backend())
                                    certificates.append(cert)
                                except ValueError as e:
                                    print(f"Erreur lors du chargement d'un certificat depuis {url}: {e}")
                    else:
                        # Traiter le contenu binaire comme un certificat DER
                        try:
                            cert = x509.load_der_x509_certificate(response.content, default_backend())
                            certificates.append(cert)
                        except ValueError as e:
                            print(f"Erreur lors du chargement d'un certificat DER depuis {url}: {e}")
                else:
                    print(f"Erreur lors du téléchargement du certificat depuis {url}: Statut {response.status_code}")
            except requests.RequestException as e:
                print(f"Erreur de requête pour {url}: {e}")
        return certificates


"""
urls = ["https://curl.se/ca/cacert.pem"]
crawler = Crawler(urls)
certificates = crawler.download_certificates()

if certificates:
    for cert in certificates:
        #print("Certificat chargé avec succès :")
        #print(cert)
        pem_cert = cert.public_bytes(encoding=serialization.Encoding.PEM)
        print(pem_cert.decode('utf-8'))
else:
    print("Il y a eu des erreurs lors du téléchargement ou du chargement des certificats.")

# pem_cert = cert.public_bytes(encoding=serialization.Encoding.PEM)
# print(pem_cert.decode('utf-8'))
"""
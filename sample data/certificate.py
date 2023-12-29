from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
from cryptography.hazmat.primitives import serialization
from crawler import Crawler
class Certificate:
    def __init__(self, cert):
        """
        Initialise un objet Certificate avec un certificat X509.
        :param cert: Certificat X509 (objet x509.Certificate).
        """
        self.cert = cert

    def extract_public_key(self):
        """
        Extrait la clé publique du certificat.
        Retourne la clé publique au format PEM.
        """
        public_key = self.cert.public_key()
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem_public_key.decode('utf-8')

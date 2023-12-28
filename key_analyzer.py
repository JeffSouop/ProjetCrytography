from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509 import Certificate
from crawler import Crawler
from certificate import Certificate


class KeyAnalyzer:
    def __init__(self, certificates):
        """
        Initialise le KeyAnalyzer avec une liste de certificats.
        :param certificates: Liste des objets Certificate représentant les certificats X509.
        """
        self.certificates = certificates


    @staticmethod
    def compare_rsa_public_keys(key1, key2):
        """
        Fonction de comparaison personnalisée pour trier les clés RSA.
        """
        # Compare la longueur de la clé (nombre de bits)
        if key1.key_size < key2.key_size:
            return -1
        elif key1.key_size > key2.key_size:
            return 1
        # Si les longueurs sont égales, compare les valeurs hexadécimales
        return (int(key1.public_numbers().encode('hex'), 16) >
                int(key2.public_numbers().encode('hex'), 16)) - \
               (int(key1.public_numbers().encode('hex'), 16) <
                int(key2.public_numbers().encode('hex'), 16))

    def sort_keys(self):
        """
        Trie les clés publiques des certificats.
        Retourne une liste triée de clés publiques.
        """
        public_keys = [cert.public_key() for cert in self.certificates]
        sorted_keys = sorted(public_keys, key=lambda key: key.key_size)
        return sorted_keys

    def find_duplicates(self):
        """
        Trouve les clés publiques en double dans la liste.
        Retourne une liste de clés publiques en double.
        """
        seen = set()
        duplicates = []
        for key in self.certificates:
            if key in seen:
                duplicates.append(key)
            else:
                seen.add(key)
        return duplicates

    def find_common_factors(self):
        """
        Identifie des clés publiques avec des facteurs communs.
        Retourne une liste de paires de clés ayant des facteurs communs.
        """
        common_factors = []
        public_keys = [cert.public_key() for cert in self.certificates]

        for i, key1 in enumerate(public_keys):
            for j, key2 in enumerate(public_keys):
                if i < j:  # Pour éviter les doublons et comparer une seule fois chaque paire
                    # Récupérer les composants N (module) des clés RSA
                    n1 = key1.public_numbers().n
                    n2 = key2.public_numbers().n
                    # Vérifier si les modules ont un facteur commun
                    if rsa.rsa_crt_iqmp(n1, n2) is not None:
                        common_factors.append((self.certificates[i], self.certificates[j]))

        return common_factors



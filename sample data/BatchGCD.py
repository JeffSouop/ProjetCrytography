from certificate import Certificate
from crawler import Crawler
from key_analyzer import KeyAnalyzer


class BatchGCD:
    def __init__(self, certificates):
        """
        Initialise BatchGCD avec une liste de certificats.
        :param certificates: Liste de certificats X509.
        """
        self.certificates = certificates

    def find_common_factors(self):
        """
        Utilise KeyAnalyzer pour trouver des paires de clés avec des facteurs communs dans les certificats.
        :return: Liste de paires de certificats avec des clés ayant des facteurs communs.
        """
        # Utilisez KeyAnalyzer pour analyser les clés publiques
        key_analyzer = KeyAnalyzer(self.certificates)
        common_factor_pairs = key_analyzer.find_common_factors()

        return common_factor_pairs


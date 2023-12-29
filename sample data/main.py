from conversion import Conversion
from crawler import Crawler


def main():
    pass
    # Chemin vers les fichiers
    # links_file_path = "links.txt"
    # keys_file_path = "keys.txt"
    # certificates_file_path = "certificats.txt"

    # conversion = Conversion()
    # links = conversion.read_links_from_file(links_file_path)
    # crawler = Crawler(links)

    # Téléchargement des certificats
    # certificates = crawler.download_certificates()

    # conversion.save_certificates_to_file(certificates_file_path, certificates)

    # Extraction des clés publiques
    # keys = [cert.public_key() for cert in certificates]

    # conversion.save_keys_to_file(keys_file_path, keys)

    # Analyse des clés (exemple d'utilisation de KeyAnalyzer, si nécessaire)
    # key_analyzer = KeyAnalyzer()
    # key_analyzer.analyze_keys(keys)

    # Application de BatchGCD sur les clés (si nécessaire)
    # batch_gcd = BatchGCD(keys)
    # gcd_results = batch_gcd.run()

if __name__ == "__main__":
    conversion = Conversion()
    conversion.run()


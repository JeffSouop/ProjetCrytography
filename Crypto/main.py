from Crypto.batch_gcd import GCDProcessor
from Crypto.calcul_module import CertificateProcessor
from extract_certificates import CertificateExtractor
from extract_keys import process_certificates
from doublons import process


def main():
    extractor = CertificateExtractor('domain.txt', 'certificat.txt')

    extractor.extract_certificates()

    process_certificates('certificat.txt', 'keys.txt')

    process('keys.txt', 'doublons.txt')

    processor = CertificateProcessor('certificat.txt', '../Crypto/informations_certificats.csv')
    processor.process_certificates()

    gcd_processor = GCDProcessor('../Crypto/informations_certificats.csv')
    gcd_processor.find_compromised_pairs()


if __name__ == "__main__":
    main()

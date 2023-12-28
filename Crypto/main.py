from extract_certificates import CertificateExtractor
from extract_keys import process_certificates
from doublons import process


def main():
    extractor = CertificateExtractor('domain.txt', 'certificat.txt')

    extractor.extract_certificates()

    process_certificates('certificat.txt', 'keys.txt')

    process('keys.txt', 'doublons.txt')


if __name__ == "__main__":
    main()

import subprocess


class CertificateExtractor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def extract_certificates(self):
        with open(self.input_file, 'r') as file:
            domain_names = file.read().splitlines()

        with open(self.output_file, 'w') as cert_file:
            for domain in domain_names:
                command = f"openssl s_client -connect {domain}:443 -showcerts"
                result = subprocess.run(["bash", "-c", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True)
                certificates = self._extract_certificates(result.stdout)
                for cert in certificates:
                    cert_file.write(cert + '\n')

    def _extract_certificates(self, output):
        certificates = []
        in_certificate = False
        lines = output.split('\n')
        for line in lines:
            if "-----BEGIN CERTIFICATE-----" in line:
                in_certificate = True
                certificate = line + '\n'
            elif "-----END CERTIFICATE-----" in line:
                in_certificate = False
                certificate += line + '\n'
                certificates.append(certificate)
            elif in_certificate:
                certificate += line + '\n'
        return certificates

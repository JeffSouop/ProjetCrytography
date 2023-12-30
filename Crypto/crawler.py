import requests


class CertificateFetcher:
    @staticmethod
    def fetch_certificates(num_certificates):
        cert_file = open('certificat.txt', 'w')

        for i in range(1, num_certificates + 1):
            url = f"https://crt.sh/?d={i}"
            response = requests.get(url)

            if response.status_code == 200:
                cert_file.write(response.text)
                cert_file.write("\n\n")
            else:
                print(f"Failed to fetch certificate {i}")

        cert_file.close()
        print(f"{num_certificates} certificats ont été téléchargé et enregistré dans certificat.txt")


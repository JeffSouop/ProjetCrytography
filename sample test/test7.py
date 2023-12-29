def convert_to_single_line(public_key):
    return ''.join(public_key.splitlines()[1:-1])

def process_keys(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        keys = data.split('-----BEGIN PUBLIC KEY-----')[1:]
        for key in keys:
            formatted_key = '-----BEGIN PUBLIC KEY-----' + convert_to_single_line(key)
            print(formatted_key)

file_path = '../Crypto/keys.txt'  # Mettez le chemin vers votre fichier contenant les clés
process_keys(file_path)

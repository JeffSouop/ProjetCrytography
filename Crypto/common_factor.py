from Crypto.PublicKey import RSA

def read_public_keys_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            keys = file.read().split('\n\n')  # Supposant que les clés sont séparées par des sauts de ligne
        return keys
    except FileNotFoundError:
        print(f"Le fichier {file_path} est introuvable.")
        return []

def compare_keys(keys):
    compromised_pairs = []

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            try:
                key_i = RSA.import_key(keys[i])
                key_j = RSA.import_key(keys[j])

                # Comparaison des modules (n) des clés RSA
                if key_i.n == key_j.n:
                    compromised_pairs.append((keys[i], keys[j]))

                # Ici, vous pouvez ajouter d'autres critères de comparaison
                # Par exemple, vérification des paramètres communs, etc.

            except ValueError:
                # Si une clé n'est pas valide, passe à la suivante
                continue

    return compromised_pairs

file_path = 'keys.txt'  # Remplacez par le chemin de votre fichier
keys = read_public_keys_from_file(file_path)

if keys:
    compromised_pairs = compare_keys(keys)

    if compromised_pairs:
        print("Paires de clés compromises :")
        for pair in compromised_pairs:
            print(pair)
    else:
        print("Aucune paire de clés compromises trouvée.")
else:
    print("Aucune clé publique trouvée dans le fichier.")

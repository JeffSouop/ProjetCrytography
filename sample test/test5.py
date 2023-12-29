def count_keys_in_file(file_path, key_type):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

            if key_type == 'public':
                # Compter les clés publiques
                public_keys_count = file_content.count('-----BEGIN PUBLIC KEY-----')
                return public_keys_count
            elif key_type == 'private':
                # Compter les clés privées
                private_keys_count = file_content.count('-----BEGIN PRIVATE KEY-----')
                return private_keys_count
            else:
                print("Type de clé non valide. Utilisez 'public' ou 'private'.")
                return 0
    except FileNotFoundError:
        print(f"Le fichier {file_path} est introuvable.")
        return 0  # Retourne 0 si le fichier est introuvable

file_path = '../Crypto/doublons.txt'  # Remplacez ceci par le chemin de votre fichier
key_type = 'public'  # Changez ceci en 'private' si vous voulez compter les clés privées
number_of_keys = count_keys_in_file(file_path, key_type)
print(f"Le nombre de clés {key_type} dans le fichier est : {number_of_keys}")

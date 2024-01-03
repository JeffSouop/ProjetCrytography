import os

# Chemin du dossier contenant les certificats
dossier_certificats = 'C:\\Users\\audrey-jordan.souop\\Downloads\\Dossier certificat\\Dossier certificat'

# Chemin du fichier où copier les certificats
chemin_fichier_copie = 'cert.txt'

# Ouvrir le fichier en mode écriture
with open(chemin_fichier_copie, 'w') as fichier_copie:
    num_certificat = 0  # Initialisation du compteur de certificats
    # Parcourir tous les fichiers du dossier des certificats
    for fichier in os.listdir(dossier_certificats):
        chemin_fichier = os.path.join(dossier_certificats, fichier)
        if os.path.isfile(chemin_fichier):
            num_certificat += 1  # Incrémenter le compteur à chaque certificat lu
            # Lire le contenu du fichier de certificat
            with open(chemin_fichier, 'r') as certificat:
                contenu_certificat = certificat.read()
                # Écrire le numéro du certificat dans le fichier de copie
                fichier_copie.write(contenu_certificat)
                fichier_copie.write("\n\n")  # Ajouter une ligne vide entre les certificats

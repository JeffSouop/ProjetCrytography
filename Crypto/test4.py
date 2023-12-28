import pandas as pd

# Charger le fichier CSV contenant les informations des certificats
file_path = 'informations_certificats.csv'

# Lire le fichier CSV
data = pd.read_csv(file_path)

# Vérifier les doublons dans la colonne 'CN'
doublons_CN = data[data.duplicated('CN', keep=False)]

# Afficher les doublons de la colonne 'CN'
if not doublons_CN.empty:
    print("Certificats avec des Common Names (CN) en double :")
    print(doublons_CN[['CN']])
else:
    print("Aucun doublon dans les Common Names (CN) des certificats.")

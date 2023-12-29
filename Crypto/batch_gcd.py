from math import gcd
from itertools import combinations
import csv

class GCDProcessor:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def batch_gcd(self, *args):
        gcds = []
        comb = combinations(args, 2)
        for pair in comb:
            gcds.append(gcd(pair[0], pair[1]))
        return gcds

    def find_compromised_pairs(self):
        modules = []
        with open(self.csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                module = row["module"]
                if module:
                    modules.append(int(module))

        indices = list(range(len(modules)))
        pairs = combinations(indices, 2)

        compromised_pairs = []

        for pair in pairs:
            result_gcd = self.batch_gcd(modules[pair[0]], modules[pair[1]])
            if result_gcd != [1]:
                x = modules[pair[0]]
                y = modules[pair[1]]

                cle_x, cle_y = None, None

                with open(self.csv_file, 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        module_val = row["module"]
                        if module_val.isdigit():  # Vérification si c'est un nombre
                            if int(module_val) == x:
                                cle_x = row["cle_publique"]
                            if int(module_val) == y:
                                cle_y = row["cle_publique"]

                if cle_x and cle_y:
                    compromised_pairs.append((cle_x, cle_y))

        with open('compromise_key.txt', 'w') as file:
            for pair in compromised_pairs:
                file.write(f"{{{pair[0]}, {pair[1]}}}\n")


import csv

# pour écrire dans un fichier pour la premiere fois
with open("file.csv", "w", newline='') as fichier: # r=read, a=append, w=write
  fieldnames = list() # la liste des cles de notre dictionnaire
  writer = csv.DictWriter(fichier, fieldnames=fieldnames)
  writer.writeheader()  # permet d'écrire les clés sur la premiere ligne du fichier
  for row in ma_liste_de_dict:
    writer.writerow(row)
    
# pour ajouter des lignes à un fichier déjà créer en utilisant la methode 
# DictWriter il suffit d'enlever la ligne writer.writeheader
# attention cependant à bien conserver les mêmes cles que ce la premiere ligne

# pour lire un fichier
with open("file.csv", "r", newline='') as fichier:
  reader = csv.DictReader(fichier)
  for row in reader:
    print(row) # va imprimer un dictionnaire correspondant à ce qui etait enregistre
    

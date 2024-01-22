# TODO : Créer un script Python pour saisir et publier des découvertes planétaires sur un blog intergalactique.

planet = input("Entrez le nom de la planete exploree: ")
date_of_visit = input("Entrez la date de votre visite (JJ/MM/AAAA): ")
description = input("Decrivez la planete: ")

print("Votre exploration a ete ajoutee au Journal des Astres !")
print(31*"-")
print(f"Titre : Decouverte de {planet}")
print(f"Date : {date_of_visit}")
print(f"Description : {description}")

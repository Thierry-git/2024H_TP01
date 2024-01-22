# TODO : Créer un script Python pour saisir et publier des découvertes planétaires sur un blog intergalactique.

planet = input("Entrez le nom de la planete explorée: ")
date_of_visit = input("Entrez la date de votre visite (JJ/MM/AAAA) :")
description = input("Décrivez la planète :")

print("Votre exploration a été ajoutée au Journal des Astres!")
print(32*"-")
print(f"Titre : Découverte de la planète {planet}")
print(f"Date : {date_of_visit}")
print(f"Description : {description}")

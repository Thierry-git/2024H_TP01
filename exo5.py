# TODO : Créer un système d'alerte qui demande le niveau de charge de la batterie, affiche une représentation graphique si la charge est entre 0 et 100%, et affiche un message d'erreur en cas de charge en dehors de la plage normale.

# Get charge level from user
charge_level = int(input("Entrez le niveau de charge actuel de la batterie : "))

# Invalid charge value
if charge_level < 0 or 100 < charge_level:
    print("Erreur : niveau de charge invalide.")
# Valid charge value
else:
    rounded_charge_units = round(charge_level, -1) // 10
    print('[' + rounded_charge_units * '❚' + (10 - rounded_charge_units) * ' ' + ']')
    print(f"{charge_level}%")

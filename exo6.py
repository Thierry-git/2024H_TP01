# TODO : Écrire un programme qui demande le pourcentage de charge actuel de la batterie de la Batmobile, calcule le temps restant en minutes en fonction de ce pourcentage, et affiche le résultat au format "XXhYYmin". Assurer la gestion des pourcentages valides et des messages d'erreur appropriés.

# Upper bounds of the different ranges, in percentage points.
# The 0 in the last spot is only accessed at the first step of the computation, via a -1 index
ranges = (5, 50, 100, 0)
weights = (5, 2, 1) # In minutes per percentage point in the corresponding range

charge_level = int(input("Entrez le pourcentage de charge actuel de la batterie de la Batmobile : "))

# Invalid charge value
if charge_level < 0 or 100 < charge_level:
    print("Erreur : niveau de charge invalide.")
# Valid charge value
else:
    # How much charge is contributed in each of the ranges
    charge_in_ranges = [ max(min(charge_level, ranges[i]) - ranges[i-1], 0) for i in range(len(ranges)-1) ]

    # Total battery time, in minutes
    battery_time = sum([charge_in_ranges[i] * weights[i] for i in range(len(ranges)-1)])

    battery_hours, battery_minutes = divmod(battery_time, 60)

    print(f"Temps restant : {battery_hours}h" + str(battery_minutes).zfill(2))

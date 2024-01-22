# TODO : Calculer la distance que chaque rocher lancé par les catapultes peut atteindre en utilisant la formule de la portée d'un projectile.
import math

g = 9.81
vitesse_initiale = float(input("Entrez la vitesse initiale (en m/s) : "))
angle_lancement_degres = float(input("Entrez l'angle de lancement (en degres) : "))

angle_lancement_radians = angle_lancement_degres * math.pi / 180

portee = (vitesse_initiale ** 2) * math.sin(2 * angle_lancement_radians) / g
portee_formattee = "{:.2f}".format(portee)

# Figure out comment print 37.10 au lieu de 37.1
print(f"La distance parcourue par le projectile est de {portee_formattee} metres.")

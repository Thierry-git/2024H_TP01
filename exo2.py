# TODO : Calculer les quantités de matériaux nécessaires pour fabriquer un nombre donné de baguettes magiques.

wand_ingredients = ("piece(s) de bois",
                    "coeur(s) de creatures magiques",
                    "ml de vernis")
wand_ingredient_weights = (3, 1, 10)

wand_qty = int(input("Nombre de baguettes a fabriquer : "))
print(f"Voici les materiaux requis pour la fabrication de {wand_qty} baguettes magiques:")
for i in range(len(wand_ingredients)):
    print(f"- {wand_qty * wand_ingredient_weights[i]} {wand_ingredients[i]}")

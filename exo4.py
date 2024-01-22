# TODO : Analyser le message crypté de l'Empire, compter le nombre d'occurrences des voyelles "a", "e", "i", "o", "u" et "y", puis assembler les résultats en une coordonnée galactique.

message = input("Entrez le message de l'Empire : ")

# Get [#a, #e, #i, #o, #u, #y]
# Note the use of .lower() in order to count capital vowels
counts = [message.lower().count(vowel) for vowel in 'aeiouy']
# Remove brackets, replace commas by periods, add final period
coordinates = str(counts).strip('[ ]').replace(", ", ".") + '.'

print(f"Les coordonnees galactiques sont {coordinates}")

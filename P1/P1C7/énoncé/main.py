# Écrivez votre code ici !

# créer le dictionnaire
fruits = {
    "pomme" : "rouge",
    "banane" : "jaune",
    "orange" : "orange"
}

# ajouter clé kiwi avec valeur vert dans le dictionnaire
fruits["kiwi"] = "vert"
print(fruits)

# Accédez à la valeur correspondant à la clé  banane  et stockez-la dans une variable appelée  couleur_banane
couleur_banane = fruits["banane"]
print(couleur_banane)

# Modifiez la valeur associée à la clé  pomme  pour  vert  .
fruits["pomme"] = "vert" 
print(fruits)

# Supprimez la clé  banane  du dictionnaire  fruits  .
del fruits["banane"]


# Affichez les clés restantes dans le dictionnaire.
print(fruits.keys())
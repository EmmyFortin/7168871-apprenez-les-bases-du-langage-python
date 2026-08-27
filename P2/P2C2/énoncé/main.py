# Ecrivez votre code ici !
# Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : "1,2,3,4").
nombres = input("Entrez une liste de nombres séparées par des virgules")

# Utilisez la fonction split(explication de la fonction) pour transformer cette chaîne de caractères en une variable de type liste  liste.listeest une liste de chaîne de caractères.
liste = nombres.split(",")
print("Liste des nombres:", liste)

# Transformezlisteen une liste d'entiersliste_entiers, en utilisant la fonction  int. Vous devrez convertir chaque élément un par un ! Utilisez une boucle.
liste_entiers = []

for nombre in liste:
    nombre_entier = int (nombre)
    liste_entiers.append(nombre_entier)

# Calculez et affichez la somme des nombres dans la liste.

somme = 0
for nombre in liste_entiers:
    somme += nombre

print("Somme des nombres:", somme)

# Effectuer la moyenne à l'aide de la somme des nombre
moyenne = somme / len(liste_entiers)

print("Moyenne des nombres:", moyenne)

# Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne.
nombre_au_dessus_moyenne = 0

for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
print("Nombre de nombres supérieurs à la moyenne:", nombre_au_dessus_moyenne)


nombres_pairs = 0
for nombre in liste_entiers:
    if nombre % 2 == 0:
        nombres_pairs = nombres_pairs + 1
        
print("Nombre de nombres pairs:", nombres_pairs)
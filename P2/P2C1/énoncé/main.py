# Ecrivez votre code ici !
# Demandez à l'utilisateur de fournir deux nombres avec la fonction input. Stockez ces valeurs dans  nombre1et  nombre2.
nombre1 = input("entrez un nombre: ")
nombre2 = input("entrez un autre nombre: ")

# nombre1et  nombre2sont des chaînes de caractères (str). Utilisez la méthode isnumeric  (explication de la méthode) pour vérifier que ce sont des nombres.

# Si ce n'est pas le cas, sortez du programme en générant une exception avec le mot cléraise:raise SystemExit("Fin du programme")
if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")

# Sinon, convertissez les deux nombres en nombres entiers avec la fonction  int.

nombre1 = int(nombre1)
nombre2 = int(nombre2)

# Créez une variableoperationet utilisezinputpour obtenir l'opération souhaitée par l'utilisateur.

operation = input("choissiez un opérateur")

# Vérifiez que l'opération est valide (+, -, * ou /). Sinon, quittez le programme.
# Effectuez le calcul en fonction de la valeur deoperation(par exemple en utilisant if - elif - else) et stockez le résultat dans la variableresultat.
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*": 
    resultat = nombre1 * nombre2
elif operation == "/":
    if nombre2 == 0:
        print("Erreur: impossible de diviser par 0")
        raise SystemExit("Fin du programme")
    resultat = round(nombre1 / nombre2, 2)

# Affichez le resultat.
print(f"Le résultat de l'opération est: {round(resultat, 2)}")
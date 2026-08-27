# Ecrivez votre code ici

# Créez une fonction appelée  salaire_mensuel(salaire_annuel)  qui prend en paramètre un salaire annuel et retourne le salaire mensuel correspondant en divisant le salaire annuel par 12.
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12
  

# Créez une fonction appelée  salaire_hebdomadaire(salaire_mensuel)  qui prend en paramètre un salaire mensuel et retourne le salaire hebdomadaire correspondant en divisant le salaire mensuel par 4.
def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4


# Créez une fonction appelée  salaire_horaire(salaire_hebdomadaire, heures_travaillees)  qui prend en paramètres un salaire hebdomadaire et le nombre d'heures travaillées par semaine, et retourne le salaire horaire correspondant en divisant le salaire hebdomadaire par le nombre d'heures travaillées par semaine.
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
   return salaire_hebdomadaire / heures_travaillees


# Demandez à l'utilisateur de saisir son salaire annuel.
salaire_annuel = float(input("Entrez votre salaire annuel: "))

# Demandez à l'utilisateur de saisir le nombre d'heures travaillées par semaine.
heures_travaillees = float(input("Entrez le nombre d'heures travaillées par semaine: "))

# Appelez les fonctions précédemment créées pour calculer le salaire horaire correspondant.
mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, heures_travaillees)

# Affichez le résultat sous la forme : "Votre salaire horaire est de XX euros".
print("Votre salaire horaire est de ", horaire,  "dollars")
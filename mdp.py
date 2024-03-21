def generer_mdp(phrase):
    mdp = ""
    correspondances = {'l': '1', 'a': '@', 's': '$', 'o': '0'}

    for mot in phrase.split():
        # Ajout du premier caractère du mot
        mdp += mot[0]

    # Remplacement des lettres spécifiées
    for lettre, speciale in correspondances.items():
        mdp = mdp.replace(lettre, speciale)

    return mdp

def saisir_option():
    while True:
        option = input("1. Continuer, 2. Quitter, 3. Afficher les phrases enregistrées: ")
        if option in ['1', '2', '3']:
            return option
        else:
            print("Option invalide. Veuillez entrer 1, 2 ou 3.")

# Nom du fichier pour enregistrer les phrases
nom_fichier = "phrases_enregistrees.txt"
phrases_enregistrees = []

while True:
    # Saisie de la phrase par l'utilisateur
    phrase_utilisateur = input("Entrez une phrase pour générer le mot de passe : ")

    # Génération du mot de passe
    mdp_genere = generer_mdp(phrase_utilisateur)

    # Affichage du mot de passe généré
    print("Mot de passe généré :", mdp_genere)

    # Saisie de l'option
    option = saisir_option()

    if option == '2':
        print("Fin de la saisie")
        break
    elif option == '3':
        print("Liste de toutes les phrases enregistrées :", phrases_enregistrees)
    else:
        # Enregistrement de la phrase dans le fichier
        with open(nom_fichier, 'a') as f:
            f.write(f"Phrase: {phrase_utilisateur}\n")

        # Ajout de la phrase à la liste des phrases enregistrées
        phrases_enregistrees.append(phrase_utilisateur)

print("Fin du programme.")

"""
J'étais en train de me faire chier donc j'ai codé ça, normalement ça marche complètement.
"""

import random as r
import qcm


def calcul_res(liste, mode):
    """calcule le résultat au questionnaire
    pre : liste est une liste comportant les réponses au questionnaire présentées sous forme de tuple dont le premier
          élément est un booléen disant si la répons eétait bonne et le deuxième disant le nombre de réponses possibles.
          Exemple : [(True, 5), (False, 3), ...]
    post : retourne un str du résultat"""
    result = 0
    if mode == "GENTIL" or mode == "1":
        for res in liste:
            if res[0]:
                result += 1
    elif mode == "méchant".upper() or mode == "2":
        for res in liste:
            if res[0]:
                result += 1
            else:
                result -= 1
    else:
        for res in liste:
            if res[0]:
                result += 1
            else:
                result -= 1 / (res[1] - 1)  # voir feuille Béranger pour calculs

    return str(round(result, 2)) + "/" + str(len(liste))


def ordre_aleatoire(liste):
    """ Détermine un ordre aléatoire pour l'affichage des questions ou des réponses ou de n'importe quoi
    pre : questionnaire est une liste présentée dans le format des listes qui sortent de la fonction
          qcm.build_questionnaire()
    post : retourne une liste dont le nombre d'éléments est égal au nombre d'éléments de questionnaire et comportant les
           int de 0 à ce nombre dans un ordre aléatoire. Exemple pcq explication pas claire: si len(questionnaire) == 5,
           la fonction peut return la liste suivante : [4, 3, 0, 2, 1] """
    ordre = [i for i in range(len(liste))]
    r.shuffle(ordre)
    return ordre


def print_reponses(reponses):
    """ Affiche les réponses à une question dans un ordre aléatoire
    pre : réponses est la liste des réponses à une question
    post : affiche les réponses dans un ordre aléatoire """
    lettres = [i + " : " for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    ordre_rep = ordre_aleatoire(reponses)
    for i in range(len(reponses)):
        a_afficher = str(lettres[i]) + str(reponses[ordre_rep[i]][0])
        print(a_afficher)
        reponses[ordre_rep[i]].append(lettres[i][0])  # permet de garder en mémoire quelle réponse est assignée à
        # quelle lettre pour la fonction qui voit si la réponse est bonne ou pas
    print("")


def demande_rep(reponses):
    """
    pre : reponses est une liste des réponses à une question sur le format ['réponse', True ou False, 'commentaire',
          "identifiant de la réponse selon le questionnaire (bon ça c'est pas clair mais en gros c'est juste pour dire
          que si dans la fenêtre d'affichage il est mis A devant la réponse et bah ici il y aura un A)"]
    post : retourne True si l'utilisateur a entré une bonne réponse, False sinon. Si plusieurs réponses étaient bonnes
           pour une question, l'utilisateur doit avoir entré toutes les bonnes réponses pour avoir le point, sinon il
           s'est trompé.
    """
    rep = input("Votre réponse : ").upper()
    print("")
    reponses_utilisateur = []
    reponses_donnees = 0
    reponses_bonnes = 0

    for caract in rep:  # ajoute toutes les réponses de l'utilisateur dans une liste
        if caract in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            reponses_utilisateur.append(caract)

    for elem in reponses:
        if elem[-1] in reponses_utilisateur:
            if elem[1]:
                reponses_donnees += 1
        if elem[1]:
            reponses_bonnes += 1

    return reponses_bonnes == reponses_donnees


def print_result(reponses, mode):
    """ Affiche le résultat à la fin du jeu
    pre : reponses : liste des réponses du joueur
          mode : str du mode de jeu choisi par l'utilisateur
    post : """
    result = calcul_res(reponses, mode)
    print("Votre résultat est de " + result)


def play_questionnaire(questionnaire):
    """ Affiche le questionnaire
    """
    ordre_quest = ordre_aleatoire(questionnaire)  # génère l'ordre dans lequel les questions vont être affichées
    liste_rep = []
    modes = ("méchant".upper(), "GENTIL", "NEUTRE", "1", "2", "3")
    typ=0
    while typ!='1' and typ!='2':
        typ = input("Quel type d'évaluation voulez-vous ? Comparatif d'évaluation (1) ou évaluation (2) ? ").upper()
    if typ == "évaluation".upper() or typ == "2":
        mode = input("Quel mode d'évaluation voulez-vous ? Gentil (1), méchant (2) ou neutre (3) ? ").upper()
        if mode not in modes :  # renvoie un code d'erreur si le mode de jeu n'existe pas
            raise KeyError("Ce mode de jeu n'existe pas")

    print()
    print("Pour répondre à chaque question, veuillez entrer les lettres des réponses que vous estimez en majuscules ou en minuscule, séparées ou pas.")
    print()
    
    for i in ordre_quest:
        print(questionnaire[i][0])
        print_reponses(questionnaire[i][1])
        to_append = (demande_rep(questionnaire[i][1]), len(questionnaire[i][1]))
        liste_rep.append(to_append)  # crée la liste des réponses sur le format [(True, 5), ...]
        if typ != "évaluation".upper() and typ != "2":
            print("En mode gentil, votre résultat jusqu'ici est de " + calcul_res(liste_rep, "GENTIL"))
            print("En mode méchant, votre résultat jusqu'ici est de " + calcul_res(liste_rep, "MÉCHANT"))
            print("En mode neutre, votre résultat jusqu'ici est de " + calcul_res(liste_rep, "NEUTRE"), end="\n\n")

    if typ == "évaluation".upper() or typ == "2":
        print_result(liste_rep, mode)


questionnaire = qcm.build_questionnaire("QCM.txt")
play_questionnaire(questionnaire)

"""
J'étais en train de me faire chier donc j'ai codé ça, normalement ça marche complètement mais il faut encore rajouter des trucs genre au début on doit pouvoir choisir
entre deux modes : evalutation et comparatif d'évaluation. Il reste juste ça à faire si je dis pas de la merde. Pour le moment c'est que en mode évaluation.
"""

import random as r
import qcm


def calcul_res(liste, mode):
    """calcule le résultat au questionnaire
    pre : liste est une liste comportant les réponses au questionnaire présentées sous forme de tuple dont le premier élément est un booléen disant si la réponse
          était bonne et le deuxième disant le nombre de réponses possibles. Exemple : [(True, 5), (False, 3), ...] """
    result = 0
    if mode == "GENTIL":
        for res in liste:
            if res[0]:
                result += 1
    elif mode == "méchant".upper():
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
    # Exemple de présentation des résultats :
    # print("Votre score est de " + str(result) + "/" + str(len(liste)))
    return result


def ordre_aleatoire(liste):
    """ Détermine un ordre aléatoire pour l'affichage des questions ou des réponses ou de n'importe quoi
    pre : questionnaire est une liste présentée dans le format des listes qui sortent de la fonction qcm.build_questionnaire()
    post : retourne une liste dont le nombre d'éléments est égal au nombre d'éléments de questionnaire et comportant les int de 0 à
           ce nombre dans un ordre aléatoire. Exemple pcq explication pas claire: si len(questionnaire) == 5, la fonction peut return
           la liste suivante : [4, 3, 0, 2, 1]"""
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
        reponses[ordre_rep[i]].append(lettres[i][0])  # permet de garder en mémoire quelle réponse est assignée à quelle lettre
        # pour la fonction qui voit si la réponse est bonne ou pas
    print("")


def demande_rep(reponses):
    """ vraiment pas claire ahah """
    rep = input("Votre réponse : ").upper()
    print("")
    reponses_utilisateur = []
    reponses_donnees = []
    reponses_bonnes = []

    for caract in rep:              # ajoute toutes les réponses de l'utilisateur dans une liste
        if caract in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            reponses_utilisateur.append(caract)

    for elem in reponses:
        if elem[-1] in reponses_utilisateur:
            if elem[1]:
                reponses_donnees.append(True)
        if elem[1]:
            reponses_bonnes.append(True)
    return reponses_bonnes == reponses_donnees


def print_result(reponses, mode):
    """ Affiche le résultat à la fin du jeu
    pre : reponses : liste des réponses du joueur
          mode : str du mode de jeu choisi par l'utilisateur
    post : """
    result = calcul_res(reponses, mode)
    print("Votre résultat est de " + str(round(result, 2)) + "/" + str(len(reponses)))


def play_questionnaire(questionnaire):
    """ Affiche le questionnaire
    """
    ordre_quest = ordre_aleatoire(questionnaire)  # génère l'ordre dans lequel les questions vont être affichées
    liste_rep = []
    mode = input("Quel mode d'évaluation voulez-vous ? Gentil, méchant ou neutre ? ").upper()

    if mode != "méchant".upper() and mode != "GENTIL" and mode != "NEUTRE":    # renvoie un code d'erreur si le mode de
        # jeu n'existe pas
        raise KeyError("Ce mode de jeu n'existe pas")

    for i in ordre_quest:
        print(questionnaire[i][0])
        print_reponses(questionnaire[i][1])
        to_append = (demande_rep(questionnaire[i][1]), len(questionnaire[i][1]))
        liste_rep.append(to_append)         # crée la liste des réponses sur le format [(True, 5), ...]

    print_result(liste_rep, mode)


questionnaire = qcm.build_questionnaire("QCM2.txt")
play_questionnaire(questionnaire)


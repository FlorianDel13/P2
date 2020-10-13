import random as r
import qcm


def calcul_res(liste, mode):
    """calcule le résultat au questionnaire
    pre : liste est une liste comportant les réponses au questionnaire présentées sous forme de tuple dont le premier élément est un booléen disant si la réponse
          était bonne et le deuxième disant le nombre de réponses possibles. Exemple : [(True, 5), (False, 3), ...] """
    result = 0
    if mode == "gentil":
        for res in liste:
            if res[0]:
                result +=1
    elif mode == "méchant":
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
                result -= 1/(res[1] - 1)          # voir feuille Béranger pour calculs
    # Exemple de présentation des résultats :
    # print("Votre score est de " + str(result) + "/" + str(len(liste)))
    return result


def ordre_aleatoire(liste):
    """Détermine un ordre aléatoire pour l'affichage des questions
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
    lettres = ["A : ", "B : ", "C : ", "D : ", "E : ", "F : ", "G : "]
    ordre_rep = ordre_aleatoire(reponses)
    for i in range(len(reponses)):
        a_afficher = str(lettres[i]) + str(reponses[ordre_rep[i]][0])
        print(a_afficher)
    print("")


def play_questionnaire(questionnaire):
    """ Affiche le questionnaire

    """
    ordre_quest = ordre_aleatoire(questionnaire)       # génère l'ordre dans lequel les questions vont être affichées
    
    for i in ordre_quest:
        print(questionnaire[i][0])
        print_reponses(questionnaire[i][1])
        # demande_rep()
        # calcul_res()
    
    

questionnaire = qcm.build_questionnaire("QCM2.txt")
play_questionnaire(questionnaire)


def trajet(mot_origine, mot_arrivee):
    trajet = [mot_origine]
    trajet_longueur = transforme_longueur(mot_origine, mot_arrivee)
    trajet_lettre = transforme_mot(trajet_longueur[-1], mot_arrivee)
    return trajet+trajet_longueur+trajet_lettre


def transforme_longueur(mot_origine, mot_arrivee):
    trajet = list()
    mot_transforme = mot_origine
    while len(mot_transforme) > len(mot_arrivee):
        mot_transforme = reduit(mot_transforme)
        trajet.append(mot_transforme)
    while len(mot_transforme) < len(mot_arrivee):
        lettre_manquante = mot_arrivee[len(mot_transforme)]
        mot_transforme = augmente(mot_transforme, lettre_manquante)
        trajet.append(mot_transforme)
    return trajet


def reduit(mot):
    return mot[:len(mot)-1]


def augmente(mot,lettre_cible):
    return mot+lettre_cible


def transforme_mot(mot_origine, mot_arrivee):
    trajet = list()
    mot_transforme = mot_origine
    while mot_transforme != mot_arrivee:
        index_lettre, lettre_a_changer = donne_difference(mot_transforme,
                                                          mot_arrivee)
        mot_transforme = change(mot_transforme,
                                index_lettre,
                                lettre_a_changer)
        trajet.append(mot_transforme)
    return trajet


def donne_difference(mot_origine, mot_arrivee):
    mot_origine, mot_arrivee = mot_origine[::-1], mot_arrivee[::-1]
    for index, lettre in enumerate(mot_arrivee):
        if mot_origine[index] != lettre:
            return  len(mot_origine) - (index+1), lettre


def change(mot, index, lettre_a_changer):
    return mot[:index]+lettre_a_changer+mot[index+1:]


def reduit(mot):
    return mot[:len(mot)-1]

def augmente(mot,lettre_cible):
    return mot+lettre_cible


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


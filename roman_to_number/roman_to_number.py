def input_user():
    return input("entrez un chiffre romain")

def roman_to_number(roman):

    dict_de_valeur = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

    resultat = 0

    for i, letter in enumerate(roman) :

        if letter in ['I','X','C'] and i<len(roman)-1 and roman[i+1] in ['V','X','L','C','D','M']:
            resultat -= (dict_de_valeur[letter])
        else :
            resultat += dict_de_valeur[letter]

    return resultat
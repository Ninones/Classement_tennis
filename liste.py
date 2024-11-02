joueurs = [
{"Nomprenom" : "Novak Djokovic", "classement" : "N°1" , "pays" : "Serbie", "imag" : "Djokovic.png"},
{"Nomprenom" : "Daniil Medvedev", "classement" : "N°2" , "pays" : "Russie", "imag" : "Medvedev.png"},
{"Nomprenom" : "Rafael Nadal", "classement" : "N°3" , "pays" : "Espagne", "imag" : "Nadal.png"},
{"Nomprenom" : "Alexander Zverev", "classement" : "N°4" , "pays" : "Allemagne", "imag" : "Zverev.png"},
{"Nomprenom" : "Stefanos Tsitsipas", "classement" : "N°5" , "pays" : "Grèce", "imag" : "Tsitsipas.png"},
{"Nomprenom" : "Matteo Berrettini", "classement" : "N°6" , "pays" : "Italie", "imag" : "Berretini.png"},
{"Nomprenom" : "Andrey Rublev", "classement" : "N°7" , "pays" : "Russie", "imag" : "Rublev.png"},
{"Nomprenom" : "Casper Ruud", "classement" : "N°8" , "pays" : "Norvège", "imag" : "Ruud.png"},
{"Nomprenom" : "Félix Auger-Aliassime", "classement" : "N°9" , "pays" : "Canada", "imag" : "Auger-Aliassime.png"},
{"Nomprenom" : "Hubert Hurkacz", "classement" : "N°10" , "pays" : "Pologne", "imag" : "Hurkacz.png"},
{"Nomprenom" : "Jannik Sinnerz", "classement" : "N°11" , "pays" : "Italie", "imag" : "Sinnerz.png"},
{"Nomprenom" : "Cameron Norrie", "classement" : "N°12" , "pays" : "Grande-Bretagne", "imag" : "Norrie.png"},
{"Nomprenom" : "Taylor Fritz", "classement" : "N°13" , "pays" : "Etats-Unis", "imag" : "Fritz.png"},
{"Nomprenom" : "Denis Shapovalov", "classement" : "N°14" , "pays" : "Canada", "imag" : "Shapovalov.png"},
{"Nomprenom" : "Diego Schwartzman", "classement" : "N°15" , "pays" : "Argentine", "imag" : "Schwartzman.png"},
{"Nomprenom" : "Carlos Alcaraz", "classement" : "N°16" , "pays" : "Espagne", "imag" : "Alcaraz.png"},
{"Nomprenom" : "Roberto Bautista Agut", "classement" : "N°17" , "pays" : "Espagne", "imag" : "Bautista Agut.png"},
{"Nomprenom" : "Reilly Opelka", "classement" : "N°18" , "pays" : "Etats-Unis", "imag" : "Opelka.png"},
{"Nomprenom" : "Pablo Carreno Busta", "classement" : "N°19" , "pays" : "Espagne", "imag" : "Carreno Busta.png"},
{"Nomprenom" : "Nikoloz Basilashvili", "classement" : "N°20" , "pays" : "Géorgie", "imag" : "Basilashvili.png"},
]

def filtre(liste, mot_Cle):
    mot_Cle = mot_Cle.lower()
    for dico in liste:
        if mot_Cle in dico["Nomprenom"].lower() or mot_Cle in dico["pays"].lower():
            return dico






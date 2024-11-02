joueuses = [
{"Nomprenom" : "Ashleigh Barty", "classement" : "N°1" , "pays" : "Australie", "imag" : "Barty.png"},
{"Nomprenom" : "Iga Swiatek", "classement" : "N°2" , "pays" : "Pologne", "imag" : "Swiatek.png"},
{"Nomprenom" : "Maria Sakkari", "classement" : "N°3" , "pays" : "Grèce", "imag" : "Sakkari.png"},
{"Nomprenom" : "Barbora Krejcikova", "classement" : "N°4" , "pays" : "Rép.Tchèque", "imag" : "Krejcikova.png"},
{"Nomprenom" : "Aryna Sabalenka", "classement" : "N°5" , "pays" : "Biélorussie", "imag" : "Sabalenka.png"},
{"Nomprenom" : "Paula Badosa Gibert", "classement" : "N°6" , "pays" : "Espagne", "imag" : "Badosa Gibert.png"},
{"Nomprenom" : "Anett Kontaveit", "classement" : "N°7" , "pays" : "Estonie", "imag" : "Kontaveit.png"},
{"Nomprenom" : "Karolina Pliskova", "classement" : "N°8" , "pays" : "Rép.Tchèque", "imag" : "Pliskova.png"},
{"Nomprenom" : "Garbiñe Muguruza", "classement" : "N°9" , "pays" : "Espagne", "imag" : "Muguruza.png"},
{"Nomprenom" : "Ons Jabeur", "classement" : "N°10" , "pays" : "Tunisie", "imag" : "Jabeur.png"},
{"Nomprenom" : "Danielle Collins", "classement" : "N°11" , "pays" : "Etats-Unis", "imag" : "Collins.png"},
{"Nomprenom" : "Jelena Ostapenko", "classement" : "N°12" , "pays" : "Estonie", "imag" : "Ostapenko.png"},
{"Nomprenom" : "Emma Raducanu", "classement" : "N°13" , "pays" : "Grande-Bretagne", "imag" : "Raducanu.png"},
{"Nomprenom" : "Anastasia Pavlyuchenkova", "classement" : "N°14" , "pays" : "Russie", "imag" : "Pavlyuchenkova .png"},
{"Nomprenom" : "Angelique Kerber", "classement" : "N°15" , "pays" : "Allemagne", "imag" : "Kerber.png"},
{"Nomprenom" : "Victoria Azarenka", "classement" : "N°16" , "pays" : "Biélorussie", "imag" : "Azarenka.png"},
{"Nomprenom" : "Cori Gauff", "classement" : "N°17" , "pays" : "Etats-Unis", "imag" : "Gauff.png"},
{"Nomprenom" : "Elena Rybakina", "classement" : "N°18" , "pays" : "Kazakhstan", "imag" : "Rybakina.png"},
{"Nomprenom" : "Simona Halep", "classement" : "N°19" , "pays" : "Roumanie", "imag" : "Halep.png"},
{"Nomprenom" : "Elina Svitolina", "classement" : "N°20" , "pays" : "Ukraine", "imag" : "Svitolina.png"},
]

def filtre(liste, mot_Cle):
    mot_Cle = mot_Cle.lower()
    for dico in liste:
        if mot_Cle in dico["Nomprenom"].lower() or mot_Cle in dico["pays"].lower():
            return dico
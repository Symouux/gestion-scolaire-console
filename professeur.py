from personne import Personne

class Professeur(Personne):
    def __init__(self, id, nom, prenom, tel, matiere):
        super().__init__(id, nom, prenom, tel)
        self.matiere = matiere

    def afficher_infos(self):
        print(f"ID : {self.id}, Nom : {self.nom}, Prénom : {self.prenom}, "
              f"Téléphone : {self.tel}, Matière : {self.matiere}")
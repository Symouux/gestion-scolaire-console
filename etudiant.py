from personne import Personne

class Etudiant(Personne):
    def __init__(self, id, nom, prenom, age, email, tel, note1=0, note2=0, note3=0):
        super().__init__(id, nom, prenom, tel)
        self.age = age
        self.__email = email
        self.note1 = note1
        self.note2 = note2
        self.note3 = note3
    
    @property
    def email(self):
        return self.__email
    
    def afficher_infos(self):
        print(f"ID : {self.id}, Nom : {self.nom}, Prénom : {self.prenom}, "
              f"Âge : {self.age}, Email : {self.email}, Téléphone : {self.tel}")
        print(f"Notes : {self.note1}, {self.note2}, {self.note3}")

    def calculer_moyenne(self):
        notes = [self.note1, self.note2, self.note3]
        moyenne = sum(notes) / len(notes)
        print(f"La moyenne de l'étudiant {self.nom} {self.prenom} est : {moyenne:.2f}")
        return moyenne
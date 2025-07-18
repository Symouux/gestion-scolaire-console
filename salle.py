class Salle:
    def __init__(self, nom, numero):
        self.nom = nom
        self.numero = numero

    def afficher_infos(self):
        print(f"Salle : {self.nom}, Numéro : {self.numero}")
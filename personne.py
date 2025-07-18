class Personne:
    nombre = 0
    
    def __init__(self, id, nom, prenom, tel):
        self.__id = id
        self.nom = nom
        self.prenom = prenom
        self.__tel = tel
        Personne.nombre += 1
    
    @property
    def id(self):
        return self.__id
    
    @property
    def tel(self):
        return self.__tel
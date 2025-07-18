from etudiant import Etudiant
from professeur import Professeur
from salle import Salle

class ProgrammePrincipale:
    def __init__(self):
        self.etudiants = []
        self.professeurs = []
        self.salles = []
    
    def ajouter_etudiant(self):
        id = input("Entrer l'identifiant d'étudiant : ")
        
        # Check if ID already exists
        for etud in self.etudiants:
            if etud.id == id:
                print("Un étudiant avec cet ID existe déjà!")
                return

        nom = input("Entrer le nom d'étudiant : ")
        prenom = input("Entrer le prénom d'étudiant : ")

        while True:
            try:
                age = int(input("Entrer l'âge d'étudiant (18-30) : "))
                if 18 <= age <= 30:
                    break
                print("L'âge doit être compris entre 18 et 30.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        while True:
            email = input("Entrer l'email d'étudiant : ")
            if "@" in email and email.endswith(".com"):
                break
            print("L'email doit contenir '@' et se terminer par '.com'.")

        while True:
            try:
                tel = input("Entrer le numéro de téléphone d'étudiant : ")
                # Basic phone validation
                if tel.isdigit() and len(tel) >= 8:
                    break
                print("Le numéro de téléphone doit contenir au moins 8 chiffres.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")

        notes = []
        for i in range(1, 4):
            while True:
                try:
                    note = float(input(f"Entrer la note {i} (0-20) : "))
                    if 0 <= note <= 20:
                        notes.append(note)
                        break
                    print("La note doit être comprise entre 0 et 20.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

        self.etudiants.append(Etudiant(id, nom, prenom, age, email, tel, *notes))
        print(f"L'étudiant {prenom} {nom} a été ajouté avec succès!")

    def supprimer_etudiant(self):
        id_etudiant = input("Entrer l'identifiant d'étudiant à supprimer : ")
        for etudiant in self.etudiants:
            if etudiant.id == id_etudiant:
                self.etudiants.remove(etudiant)
                print(f"L'étudiant {id_etudiant} a été supprimé avec succès!")
                return
        print("Aucun étudiant trouvé avec cet ID.")

    def recherche_etudiant(self):
        id_etudiant = input("Entrer l'ID de l'étudiant à rechercher : ")
        for etudiant in self.etudiants:
            if etudiant.id == id_etudiant:
                print("\n--- Informations de l'étudiant ---")
                etudiant.afficher_infos()
                return
        print("Étudiant non trouvé.")

    def modifier_etudiant(self):
        id_etudiant = input("Entrer l'ID de l'étudiant à modifier : ")
        for etudiant in self.etudiants:
            if etudiant.id == id_etudiant:
                print("\nLaissez le champ vide pour conserver la valeur actuelle")
                
                nouveau_nom = input(f"Nom actuel: {etudiant.nom}. Nouveau nom: ")
                if nouveau_nom:
                    etudiant.nom = nouveau_nom
                
                nouveau_prenom = input(f"Prénom actuel: {etudiant.prenom}. Nouveau prénom: ")
                if nouveau_prenom:
                    etudiant.prenom = nouveau_prenom
                
                # Similar for other fields
                print("Étudiant modifié avec succès!")
                return
        print("Étudiant non trouvé.")

    def afficher_etudiants(self):
        if not self.etudiants:
            print("Aucun étudiant enregistré.")
        else:
            print("\n--- Liste des étudiants ---")
            for etudiant in self.etudiants:
                etudiant.afficher_infos()
                print("-----------------------------")

    def calculer_moyenne_etudiant(self):
        id_etudiant = input("Entrer l'ID de l'étudiant pour calculer la moyenne : ")
        for etudiant in self.etudiants:
            if etudiant.id == id_etudiant:
                moyenne = etudiant.calculer_moyenne()
                return moyenne
        print("Étudiant non trouvé.")
        return None

    def ajouter_professeur(self):
        id = input("Entrer l'identifiant du professeur : ")
        
        # Check if ID exists
        for prof in self.professeurs:
            if prof.id == id:
                print("Un professeur avec cet ID existe déjà!")
                return

        nom = input("Entrer le nom du professeur : ")
        prenom = input("Entrer le prénom du professeur : ")
        tel = input("Entrer le numéro de téléphone du professeur : ")
        matiere = input("Entrer la matière enseignée : ")

        self.professeurs.append(Professeur(id, nom, prenom, tel, matiere))
        print(f"Le professeur {prenom} {nom} a été ajouté avec succès!")

    def supprimer_professeur(self):
        id_professeur = input("Entrer l'identifiant du professeur à supprimer : ")
        for professeur in self.professeurs:
            if professeur.id == id_professeur:
                self.professeurs.remove(professeur)
                print(f"Le professeur {id_professeur} a été supprimé avec succès!")
                return
        print("Aucun professeur trouvé avec cet ID.")

    def afficher_professeurs(self):
        if not self.professeurs:
            print("Aucun professeur enregistré.")
        else:
            print("\n--- Liste des professeurs ---")
            for professeur in self.professeurs:
                professeur.afficher_infos()
                print("-----------------------------")

    def ajouter_salle(self):
        nom = input("Entrer le nom de la salle : ")
        numero = input("Entrer le numéro de la salle : ")
        
        # Check if room already exists
        for salle in self.salles:
            if salle.nom == nom and salle.numero == numero:
                print("Cette salle existe déjà!")
                return

        self.salles.append(Salle(nom, numero))
        print(f"La salle {nom} a été ajoutée avec succès!")

    def afficher_salles(self):
        if not self.salles:
            print("Aucune salle enregistrée.")
        else:
            print("\n--- Liste des salles ---")
            for salle in self.salles:
                salle.afficher_infos()
                print("-----------------------------")

    def menu(self):
        while True:
            print("\n--- MENU PRINCIPAL ---")
            print("1. Gestion des étudiants")
            print("2. Gestion des professeurs")
            print("3. Gestion des salles")
            print("4. Quitter")
            
            choix_principal = input("Entrez votre choix : ")
            
            if choix_principal == "1":
                self.menu_etudiants()
            elif choix_principal == "2":
                self.menu_professeurs()
            elif choix_principal == "3":
                self.menu_salles()
            elif choix_principal == "4":
                print("Au revoir!")
                break
            else:
                print("Choix invalide, veuillez réessayer.")

    def menu_etudiants(self):
        while True:
            print("\n--- MENU ÉTUDIANTS ---")
            print("1. Ajouter un étudiant")
            print("2. Supprimer un étudiant")
            print("3. Rechercher un étudiant")
            print("4. Modifier un étudiant")
            print("5. Afficher tous les étudiants")
            print("6. Calculer la moyenne d'un étudiant")
            print("7. Retour au menu principal")
            
            choix = input("Entrez votre choix : ")
            
            if choix == "1":
                self.ajouter_etudiant()
            elif choix == "2":
                self.supprimer_etudiant()
            elif choix == "3":
                self.recherche_etudiant()
            elif choix == "4":
                self.modifier_etudiant()
            elif choix == "5":
                self.afficher_etudiants()
            elif choix == "6":
                self.calculer_moyenne_etudiant()
            elif choix == "7":
                break
            else:
                print("Choix invalide, veuillez réessayer.")

    def menu_professeurs(self):
        while True:
            print("\n--- MENU PROFESSEURS ---")
            print("1. Ajouter un professeur")
            print("2. Supprimer un professeur")
            print("3. Afficher tous les professeurs")
            print("4. Retour au menu principal")
            
            choix = input("Entrez votre choix : ")
            
            if choix == "1":
                self.ajouter_professeur()
            elif choix == "2":
                self.supprimer_professeur()
            elif choix == "3":
                self.afficher_professeurs()
            elif choix == "4":
                break
            else:
                print("Choix invalide, veuillez réessayer.")

    def menu_salles(self):
        while True:
            print("\n--- MENU SALLES ---")
            print("1. Ajouter une salle")
            print("2. Afficher toutes les salles")
            print("3. Retour au menu principal")
            
            choix = input("Entrez votre choix : ")
            
            if choix == "1":
                self.ajouter_salle()
            elif choix == "2":
                self.afficher_salles()
            elif choix == "3":
                break
            else:
                print("Choix invalide, veuillez réessayer.")


# if __name__ == "__main__":
#     programme = ProgrammePrincipale()
#     programme.menu()
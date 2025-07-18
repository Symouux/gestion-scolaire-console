from programme_principale import ProgrammePrincipale

def main():
    print("\n" + "="*50)
    print("SYSTÈME DE GESTION SCOLAIRE".center(50))
    print("="*50 + "\n")
    
    programme = ProgrammePrincipale()
    programme.menu()

if __name__ == "__main__":
    main()
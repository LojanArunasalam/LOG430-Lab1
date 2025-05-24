# We need to populate the database
def populate_database():
    pass


def main():
    populate_database()
    message = """
======= CAISSE =======
1 - Rechercher un produit
2 - Enregistrer un vente
3 - Gerer un retour
4 - Consulter le stock d'un produit
5 - Exit
--------------"""

    while True:
        print(message)
        choice = int(input("Choisissez une option: "))

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            break
        else:
            continue


if __name__ == "__main__":
    main()

etudien=["mahmoud","jihad","hassan"]
note=[[12,10,20],[20,15,17],[19,18,9]]
age=[14,15,14]


def afficher():
    for i in etudien:
        print(i)


def menu():
    while True:
        print("1:ajouter etudien")
        print("2:ajouter ")
        print("5 : quiter")

        n = input("donner un nombre de menu")
        if n =="1":
            afficher()
        elif n =="5":
            return False
        else : 
            print("unvalide nombre")
menu()
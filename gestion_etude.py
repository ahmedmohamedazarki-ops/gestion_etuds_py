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
            print("unvalide nombre")etudien = ["mahmoud", "jihad", "hassan"]
note = [[15,10,19],[20,15,17],[19,18,9]]
age = [14,15,14]

def afficher_etudiant():
    for i in etudien:
        print(i)

def delete_etudiant():
    n = input("donner un nombre de etudiant: ")
    ind=-1
    for i in range(len(etudien)):
        if etudien[i] == n:
            ind=i
            break
    if ind!=-1:
        etudien.remove(etudien[ind])
        note.remove(note[ind])
        age.remove(age[ind])
    print(n,"supirmer")
    for i in etudien:
        print(i)    
    for i in note:
        print(i)
    for i in age:
        print(i)
    
def afficher_age():
    for i in age:
        print(i)
 
def recherche_etudiant():
    n = input("donner un nombre de etudiant: ")
    ind=-1
    for i in range(len(etudien)):
        if etudien[i] == n:
            ind=i
            break
    if ind!=-1:
        print(etudien[ind])
        print(note[ind])
        print(age[ind]) 
        print((sum(note[ind])/len(note[ind]))) 
    else :
        print("etudiant non trouver 😒")


def moyenne():
    for i in range(len(etudien)):
        print(etudien[i], ":", sum(note[i])/len(note[i]))

def afficher_notes():
    for i in range(len(etudien)):
        print(etudien[i], ":", note[i])

def note_max():
    for i in range(len(etudien)):
        print(etudien[i], ":", max(note[i]))

def note_min():
    for i in range(len(etudien)):
        print(etudien[i], ":", min(note[i]))
                

def menu():
    while True:
        print("1: afficher etudiants")
        print("2: afficher notes")
        print("3: afficher age")
        print("4: moyenne")
        print("5: delete etudiant")
        print("6: recherche etudiant")
        print("7: note max")
        print("8: note min")
        print("9: quitter")

        n = input("donner un nombre de menu: ")

        if n == "1":
            afficher_etudiant()
        elif n == "2":
            afficher_notes()
        elif n == "3":
            afficher_age()
        elif n == "4":
            moyenne()
        elif n == "5":
            delete_etudiant()
        elif n == "6":
            recherche_etudiant()
        elif n == "7":
            note_max()
        elif n == "8":
            note_min()    
        elif n == "9":    
            print("au revoir 👋")
            break
        else:
            print("nombre invalide 😒")

menu()
    
                
"""
Premier programme écrit en Python le 19.02.2021
    D'après la video de tuto APPRENDRE PYTHON:
        https://www.youtube.com/watch?v=oUJolR5bX6g&t=49s
"""

def afficher_nom_age(n,a):
    print("""
        Tu t'appelles %s et tu as %s ans
            Dans un an tu auras %s ans
        """ % (n, a, int(a)+1))

def demander_age():
    age = 0
    while age == 0:
        try:
            age = int(input("age? "))
        except:
            print("recommence avec nombre stp")
    return age


def demander_nom():
    nom = ""
    while nom == "":
        nom = input("nom? ")
    return nom


j: float = 0

def pairs():
    for i in range(0, 11):
        global j
        j = i/2
        if j.is_integer():
            print(f"{i} est pair")
        else:
            print("%s est impair" % i)

def divisible(n:int,d:int):
    return not d==0 and (n/d).is_integer()

def is_premier(p):
    Diviseurs = [2, 3, 5, 7]
    i = 0
    while (i<4):
        if (p/Diviseurs[i]).is_integer():
            return False
        else:
             i = i+1
    return True


def premiers100():

    liste = []
    for i in range(101):
        if is_premier(i):
            liste.append(i)
    print(liste)

#nom_str = demander_nom()
#age_int = demander_age()

print()
#afficher_nom_age(nom_str,str(age_int))
# pairs()
premiers100()

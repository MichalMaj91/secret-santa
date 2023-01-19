import random
import os
import sys
from time import sleep

lista_imion = []
lista_losujacych = [] 

while True:
    czy_dodac = input("Czy chcesz dodać imię do listy? (t/n)")
    if czy_dodac == "t":
        do_dodania = str.capitalize(str.strip(input("Podaj imię: ")))
        if do_dodania in lista_imion:
            print("Podane imię znajduje się już na liście. Podaj wartość unikatową.")
        elif len(do_dodania) == 0:
            print("Należy podać imię!")
        else:
            lista_imion.append(do_dodania)
    elif czy_dodac == "n": 
        if len(lista_imion) < 3:
            while True:
                print("Lista jest za krótka, aby móc losować osoby.")
                czy_zakonczyc = input("Czy chcesz zakończyć działanie programu? (t/n)")
                if czy_zakonczyc == "t":
                    sys.exit(0)
                elif czy_zakonczyc == "n": 
                    break
                else:
                    os.system("cls")
                    print("Podano nieprawidłową wartość.")
        else:
            break
    else:
        os.system("cls")
        print("Podano nieprawdłową odpowiedź.")

random.shuffle(lista_imion)

for i in range(len(lista_imion)):
    if i != len(lista_imion) - 1 :
        lista_losujacych.append(lista_imion[i + 1])
    else:
        lista_losujacych.append(lista_imion[0])

mikolaj = {}

for i in range (len(lista_imion)):
    mikolaj[lista_imion[i]] = lista_losujacych[i]

# print(mikolaj)

lista_do_wyswietlenia = list(mikolaj.items())

random.shuffle(lista_do_wyswietlenia)

for i in range(len(lista_imion)):
    os.system("cls")
    input("Naciśnij Enter aby kontynuować.")
    os.system("cls")
    print("Teraz losować będzie", lista_do_wyswietlenia[i][0])
    input("Naciśnij Enter aby kontynuować.")
    print(lista_do_wyswietlenia [i][0], "kupujesz prezent dla", lista_do_wyswietlenia[i][1])
    input("Naciśnij Enter aby kontynuować.")

os.system("cls")

print("To już wszyscy.")
sleep(5)

-----------------------------------------------------------------------------------

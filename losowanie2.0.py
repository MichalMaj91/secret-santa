# import random
# import os
# import sys
# from time import sleep

# lista_imion = []
# lista_losujacych = [] 

# while True:
#     czy_dodac = input("Czy chcesz dodać imię do listy? (t/n)")
#     if czy_dodac == "t":
#         do_dodania = str.capitalize(str.strip(input("Podaj imię: ")))
#         if do_dodania in lista_imion:
#             print("Podane imię znajduje się już na liście. Podaj wartość unikatową.")
#         elif len(do_dodania) == 0:
#             print("Należy podać imię!")
#         else:
#             lista_imion.append(do_dodania)
#     elif czy_dodac == "n": 
#         if len(lista_imion) < 3:
#             while True:
#                 print("Lista jest za krótka, aby móc losować osoby.")
#                 czy_zakonczyc = input("Czy chcesz zakończyć działanie programu? (t/n)")
#                 if czy_zakonczyc == "t":
#                     sys.exit(0)
#                 elif czy_zakonczyc == "n": 
#                     break
#                 else:
#                     os.system("cls")
#                     print("Podano nieprawidłową wartość.")
#         else:
#             break
#     else:
#         os.system("cls")
#         print("Podano nieprawdłową odpowiedź.")

# random.shuffle(lista_imion)

# for i in range(len(lista_imion)):
#     if i != len(lista_imion) - 1 :
#         lista_losujacych.append(lista_imion[i + 1])
#     else:
#         lista_losujacych.append(lista_imion[0])

# mikolaj = {}

# for i in range (len(lista_imion)):
#     mikolaj[lista_imion[i]] = lista_losujacych[i]

# # print(mikolaj)

# lista_do_wyswietlenia = list(mikolaj.items())

# random.shuffle(lista_do_wyswietlenia)

# for i in range(len(lista_imion)):
#     os.system("cls")
#     input("Naciśnij Enter aby kontynuować.")
#     os.system("cls")
#     print("Teraz losować będzie", lista_do_wyswietlenia[i][0])
#     input("Naciśnij Enter aby kontynuować.")
#     print(lista_do_wyswietlenia [i][0], "kupujesz prezent dla", lista_do_wyswietlenia[i][1])
#     input("Naciśnij Enter aby kontynuować.")

# os.system("cls")

# print("To już wszyscy.")
# sleep(5)

# -----------------------------------------------------------------------------------

import random
from sys import exit
import tkinter as tk

def dodaj():
    global lista_imion
    do_dodania = str.capitalize(str.strip(ent_podaj_imie.get()))
    if do_dodania in lista_imion:
        lbl_komunikaty.config(text="Podane imię jest już na liście.")
    elif len(do_dodania) == 0:
        lbl_komunikaty.config(text="Należy podać imię!")
    else:
        lista_imion.append(do_dodania)
        ent_podaj_imie.delete(0, tk.END)
        lbl_komunikaty.config(text="Dodano imię do listy.")
    


def losowanie():
    global lista_imion, lista_losujacych, lista_do_wyswietlenia, robocza, lbl_miko
    global btn_nastepny, okno_losowania
    random.shuffle(lista_imion)
    robocza = 0

    if len(lista_imion) < 3:
        lbl_komunikaty.config(text="Lista jest za krótka.")
    else:
        for i in range(len(lista_imion)):
            if i != len(lista_imion) - 1 :
                lista_losujacych.append(lista_imion[i + 1])
            else:
                lista_losujacych.append(lista_imion[0])
    
        mikolaj = {}
        for i in range (len(lista_imion)):
            mikolaj[lista_imion[i]] = lista_losujacych[i]

        lista_do_wyswietlenia = list(mikolaj.items())

        random.shuffle(lista_do_wyswietlenia)

        okno_losowania = tk.Tk()
        okno_losowania.geometry("340x100")
        okno_losowania.title("Losowanie")

        lbl_miko = tk.Label(okno_losowania, text="")
        btn_nastepny = tk.Button(okno_losowania, text="Następny.", command=rob2)
        lbl_miko.config(text="Teraz losować będzie: " + lista_do_wyswietlenia[robocza][0], font="30")
        

        lbl_miko.pack()
        btn_nastepny.place(relx=0.4, rely=0.6)
    
def nowe_losowanie():
    global lista_imion, lista_do_wyswietlenia, lista_losujacych
    lista_losujacych = []
    lista_do_wyswietlenia = []
    lista_imion = []
    lbl_komunikaty.config(text="")
    okno_losowania.destroy()

def rob():
    global robocza
    robocza += 1
    if robocza < len(lista_do_wyswietlenia):
        lbl_miko.config(text="Teraz losować będzie: " + lista_do_wyswietlenia[robocza][0])
        btn_nastepny.config(command=rob2)
    else:
        lbl_miko.config(text="To już wszyscy.")
        btn_nastepny.config(text="Zakończ", command=exit)
        btn_nowelosowanie = tk.Button(okno_losowania, text="Nowe losowanie", command = nowe_losowanie)

        btn_nastepny.place(relx=0.7, rely=0.6)
        btn_nowelosowanie.place(relx=0.1, rely=0.6)


def rob2():
    lbl_miko.config(text=lista_do_wyswietlenia[robocza][0] + " Kupujesz prezent dla " + lista_do_wyswietlenia[robocza][1])
    btn_nastepny.config(command=rob)


lista_imion = []
lista_losujacych = []

ekran_1 = tk.Tk()
ekran_1.minsize(340, 100)
ekran_1.geometry('340x100')
ekran_1.title("Losowanie na mikołajki.")

lbl_instrukcje = tk.Label(text="Wpisz imiona do losowania: ")
btn_dodaj_imie = tk.Button(text="Dodaj imię", command=dodaj)
btn_dalej = tk.Button(text="Przejdź do losowania", command=losowanie)
ent_podaj_imie = tk.Entry()
lbl_komunikaty = tk.Label(font="10")

lbl_instrukcje.place(relx=0.0, rely=0.05)
btn_dodaj_imie.place(relx=0.2, rely=0.6)
ent_podaj_imie.place(relx=0.55, rely=0.05)
btn_dalej.place(relx=0.5, rely=0.6)
lbl_komunikaty.place(relx=0.2, rely=0.25)

ekran_1.mainloop()
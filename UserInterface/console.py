import datetime
from Logic.crud import adauga_cheltuiala, modifica_cheltuiala, stergere_cheltuiala, stergere_cheltuiala_tip, \
    cautare_suma_mai_mare, cautare_cheltuiala_tip_cheltuiala, cautare_cheltuiala_data_suma, suma_totala_cheltuiala, \
    sortare_apartamente_tip_cheltuiala, total_cheltuieli_apartament, eliminare_cheltuieli_tip_cheltuiala, \
    eliminare_cheltuieli_suma, undo


def print_menu():
    print("1. Adaugati o cheltuiala")
    print("2. Modifica o cheltuiala")
    print("3. Sterge o cheltuiala")
    print("4. Stergere o cheltuiala dupa tip")
    print("5. Cautare cheltuieli mai mari decat suma scrisa")
    print("6. Cautare cheltuieli dupa o anumita descriere")
    print("7. Cautare cheltuieli cu o data inainte de cea data si o suma mai mare decat cea data la tastatura")
    print("8. Suma totala a unui tip de cheltuiala")
    print("9. Ordoneaza apartamentele dupa tipul de cheltuiala")
    print("10. Realizeaza suma totala a unui apartament a tuturor cheltuielilor")
    print("11. Eliminare cheltuieli dupa tipul de cheltuiala")
    print("12. Eliminare cheltuieli dupa o suma data la tastatura, acestea fiind sterse daca sunt mai mici")
    print("u. Undo")
    print("a. Afisare cheltuiala")
    print("x. Iesire program")


def UI_adauga_cheltuiala(lista, undo_lista):
    nr_apartament_id = int(input("Introduceti numarul apartamentului:"))
    suma = float(input("Introduceti suma dorita:"))
    tip_cheltuiala = input("Introduceti tipul de cheltuiala (apa, curent, altele, etc):")
    y = int(input("Introduceti anul 'yyyy':"))
    m = int(input("Introduceti luna 'mm':"))
    d = int(input("Introduce ziua 'dd':"))
    data = datetime.date(y, m, d)
    rezultat = adauga_cheltuiala(nr_apartament_id, suma, tip_cheltuiala, data, lista, undo_lista)
    return rezultat


def UI_modifica_cheltuiala(lista, undo_lista):
    nr_apartament_id = int(input("Introduceti numarul apartamentului:"))
    suma = float(input("Introduceti suma dorita:"))
    tip_cheltuiala = input("Introduceti tipul de cheltuiala (apa, curent, altele, etc):")
    y = int(input("Introduceti anul 'yyyy':"))
    m = int(input("Introduceti luna 'mm':"))
    d = int(input("Introduce ziua 'dd':"))
    data = datetime.date(y, m, d)
    rezultat = modifica_cheltuiala(nr_apartament_id, suma, tip_cheltuiala, data, lista, undo_lista)
    return rezultat


def UI_stergere_cheltuiala(lista, undo_lista):
    nr_apartament_id = int(input("Introduceti numarul apartamentului:"))
    rezultat = stergere_cheltuiala(nr_apartament_id, lista, undo_lista)
    return rezultat


def UI_stergere_cheltuiala_tip(lista, undo_lista):
    tip_cheltuiala = input("Introduceti tipul de cheltuiala ce doriti sa fie stearsa:")
    rezultat = stergere_cheltuiala_tip(tip_cheltuiala, lista, undo_lista)
    return rezultat


def UI_cautare_cheltuiala_mai_mare(lista):
    suma = float(input("Introduceti suma dorita:"))
    rezultat = cautare_suma_mai_mare(suma, lista)
    print(rezultat)


def UI_cautare_cheltuiala_tip_cheltuiala(lista):
    tip_cheltuiala = input("Introduceti descrierea cautata:")
    rezultat = cautare_cheltuiala_tip_cheltuiala(tip_cheltuiala, lista)
    print(rezultat)


def UI_cautare_cheltuiala_data_suma(lista):
    y = int(input("Introduceti anul 'yyyy':"))
    m = int(input("Introduceti luna 'mm':"))
    d = int(input("Introduce ziua 'dd':"))
    data = datetime.date(y, m, d)
    suma = float(input("Introduceti suma:"))
    rezultat = cautare_cheltuiala_data_suma(data, suma, lista)
    print(rezultat)


def UI_suma_totala_cheltuiala(lista):
    tip_cheltuiala = input("Introduceti tipul de cheltuiala:")
    rezultat = suma_totala_cheltuiala(tip_cheltuiala, lista)
    print(f'Suma totala a tipului de cheltuiala este: {rezultat}')


def UI_ordonare_apartamente_tip_cheltuiala(lista, undo_lista):
    rezultat = sortare_apartamente_tip_cheltuiala(lista, undo_lista)
    return rezultat


def UI_suma_totala_apartament(lista):
    nr_apartament_id = int(input("Introduceti numarul apartamentului ce doriti sa ii faceti suma totala:"))
    rezultat = total_cheltuieli_apartament(nr_apartament_id, lista)
    print(rezultat)


def UI_eliminare_cheltuiala_tip_cheltuiala(lista, undo_lista):
    tip_cheltuiala = input("Introduceti tipul de cheltuiala ce doriti sa fie sters:")
    rezultat = eliminare_cheltuieli_tip_cheltuiala(tip_cheltuiala, lista, undo_lista)
    return rezultat


def UI_eliminare_cheltuia_suma(lista, undo_lista):
    suma = int(input("Introduceti suma ce doriti sa o introduceti:"))
    rezultat = eliminare_cheltuieli_suma(suma, lista, undo_lista)
    return rezultat


def run_menu(lista):
    undo_lista =[]
    while True:
        print_menu()
        optiune = input("Introduceti optiunea dorita:")
        if optiune == '1':
            try:
                lista = UI_adauga_cheltuiala(lista, undo_lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '2':
            try:
                lista = UI_modifica_cheltuiala(lista, undo_lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '3':
            try:
                lista = UI_stergere_cheltuiala(lista, undo_lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '4':
            try:
                lista = UI_stergere_cheltuiala_tip(lista, undo_lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '5':
            try:
                UI_cautare_cheltuiala_mai_mare(lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '6':
            try:
                UI_cautare_cheltuiala_tip_cheltuiala(lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '7':
            try:
                UI_cautare_cheltuiala_data_suma(lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '8':
            try:
                UI_suma_totala_cheltuiala(lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '9':
            try:
                lista = UI_ordonare_apartamente_tip_cheltuiala(lista, undo_lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '10':
            try:
                UI_suma_totala_apartament(lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '11':
            try:
                lista = UI_eliminare_cheltuiala_tip_cheltuiala(lista, undo_lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == '12':
            try:
                lista = UI_eliminare_cheltuia_suma(lista, undo_lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            except KeyError as ke:
                print("Eroare: {}".format(ke))
        elif optiune == 'u':
            lista_noua = undo(undo_lista)
            if lista_noua is not None:
                lista = lista_noua
            else:
                print("Nu se poate face undo!")
        elif optiune == 'a':
            print(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiune introdusa gresit, reincercati!")

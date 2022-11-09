def creeaza_cheltuiala(nr_apartament_id=int, suma=float, tip_cheltuiala=str):
    return {
        'nr_apartament_id': nr_apartament_id,
        'suma': suma,
        'tip_cheltuiala': tip_cheltuiala,
    }


def adauga_cheltuiala(nr_apartament_id, suma, tip_cheltuiala, lista, undo):
    """
    Adauga o cheltuiala
    :param lista: lista cu dictionare
    :param nr_apartament_id: id-ul string
    :param suma: suma float
    :param tip_cheltuiala: descrierea
    :return: cheltuiala
    """
    cheltuiala = creeaza_cheltuiala(nr_apartament_id, suma, tip_cheltuiala)
    undo.append(lista)
    return lista + [cheltuiala]


def get_nr_apartament_id(cheltuiala):
    return cheltuiala['nr_apartament_id']


def stergere_cheltuiala(nr_apartament_id, lista, undo):
    undo.append(lista)
    return [cheltuiala for cheltuiala in lista if get_nr_apartament_id(cheltuiala) != nr_apartament_id]


def print_menu():
    print("1. Adaugati o cheltuiala")
    print("2. Sterge o cheltuiala")
    print("x. Iesire")


def UI_adauga_cheltuiala(lista, undo):
    nr_apartament_id = int(input("Introduceti numarul apartamentului:"))
    suma = float(input("Introduceti suma dorita:"))
    tip_cheltuiala = input("Introduceti tipul de cheltuiala (apa, curent, altele, etc):")
    rezultat = adauga_cheltuiala(nr_apartament_id, suma, tip_cheltuiala, lista, undo)
    return rezultat


def UI_stergere_cheltuiala(lista, undo):
    nr_apartament_id = int(input("Introduceti numarul apartamentului:"))
    rezultat = stergere_cheltuiala(nr_apartament_id, lista, undo)
    return rezultat


def undo(undo_lista):
    if len(undo_lista) > 0:
        return undo_lista.pop()
    else:
        return None


def run_menu(lista):
    undo_lista = []
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
                lista = UI_stergere_cheltuiala(lista, undo_lista)
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
        elif optiune == 'x':
            break
        elif optiune == 'a':
            print(lista)
        else:
            print("Optiune introdusa gresit, reincercati!")

run_menu([])
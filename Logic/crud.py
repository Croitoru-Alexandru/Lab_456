from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament_id, get_tip_cheltuiala, get_suma, get_data


def get_by_id(nr_apartament_id, lista):
    """
    gaseste un obiect dupa id-ul dat din lista
    :param nr_apartament_id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat din lista
    """
    for cheltuiala in lista:
        if get_nr_apartament_id(cheltuiala) == nr_apartament_id:
            return cheltuiala
    return None


def adauga_cheltuiala(nr_apartament_id, suma, tip_cheltuiala, data, lista, undo_lista):
    """
    Adauga o cheltuiala
    :param lista: lista cu dictionare
    :param nr_apartament_id: id-ul string
    :param suma: suma float
    :param tip_cheltuiala: descrierea
    :return: cheltuiala
    """
    cheltuiala = creeaza_cheltuiala(nr_apartament_id, suma, tip_cheltuiala, data)
    undo_lista.append(lista)
    return lista + [cheltuiala]


def modifica_cheltuiala(nr_apartament_id, suma, tip_cheltuiala, data, lista, undo_lista):
    """
    Modifica o cheltuiala
    :param nr_apartament_id: id - string
    :param suma: suma - float
    :param tip_cheltuiala: descriere
    :param lista: lista cu dictionare
    :return: lista noua
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_nr_apartament_id(cheltuiala) == nr_apartament_id:
            cheltuiala_noua = creeaza_cheltuiala(nr_apartament_id, suma, tip_cheltuiala, data)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    undo_lista.append(lista)
    return lista_noua


def stergere_cheltuiala(nr_apartament_id, lista, undo_lista):
    """
    stergere cheltuiala
    :param nr_apartament_id: id - string
    :param lista: lista cu dictionare
    :return: lista fara dictionarul selectat
    """
    undo_lista.append(lista)
    return [cheltuiala for cheltuiala in lista if get_nr_apartament_id(cheltuiala) != nr_apartament_id]


def stergere_cheltuiala_tip(tip_cheltuiala, lista, undo_lista):
    """
    Stergere dupa tipul de cheltuiala
    :param tip_cheltuiala: descrierea
    :param lista: lista cu dictionare
    :return: lista fara apartamentele cu tipul de cheltuiala dorit sters
    """
    undo_lista.append(lista)
    return [cheltuiala for cheltuiala in lista if get_tip_cheltuiala(cheltuiala) != tip_cheltuiala]


def cautare_suma_mai_mare(suma, lista):
    """
    Cautarea apartamentelor care au suma mai mare decat suma data
    :param suma: suma data
    :param lista: lista cu apartamente
    :return: lista cu apartamentele care au suma mai mare decat cea data
    """
    lista_noua = []
    for cheltuiala in lista:
        if suma < get_suma(cheltuiala):
            lista_noua.append(cheltuiala)
    return lista_noua


def cautare_cheltuiala_tip_cheltuiala(tip_cheltuiala, lista):
    """
    Cautarea cheltuielilor care au o anumita descriere
    :param tip_cheltuiala: anumita descriere
    :param lista: lista de dictionare
    :return: lista cu dictionarele cautate
    """
    lista_noua = []
    for cheltuiala in lista:
        if tip_cheltuiala == get_tip_cheltuiala(cheltuiala):
            lista_noua.append(cheltuiala)
    return lista_noua


def cautare_cheltuiala_data_suma(data, suma, lista):
    """
    Cautarea cheltuielilor dupa o data si suma
    :param data: data oferita
    :param suma: suma data
    :param lista: lista cu dictionarele
    :return: lista cu cheltuielilor inaintea datei date si cu o suma mai mare decat cea data
    """
    lista_noua = []
    for cheltuiala in lista:
        if data > get_data(cheltuiala) and suma < get_suma(cheltuiala):
            lista_noua.append(cheltuiala)
    return lista_noua


def suma_totala_cheltuiala(tip_cheltuiala, lista):
    """
    Realizarea sumei totale pe un tip de cheltuiala
    :param tip_cheltuiala: descrierea cheltuielii
    :return: Suma totala a acelei cheltuieli
    """
    suma_totala = 0
    lista_noua = []
    for cheltuiala in lista:
        if get_tip_cheltuiala(cheltuiala) == tip_cheltuiala:
            lista_noua.append(cheltuiala)
    for suma in lista_noua:
        suma_totala = suma_totala + get_suma(suma)
    return suma_totala


def sortare_apartamente_tip_cheltuiala(lista, undo_lista):
    """
    Sorteaza toate apartamentele dupa tipul de cheltuiala
    :param lista: lista cu dictionare
    :return: lista in ordine dupa tipul de cheltuiala
    """
    undo_lista.append(lista)
    return sorted(lista, key=lambda tip_cheltuiala: get_tip_cheltuiala(tip_cheltuiala))


def total_cheltuieli_apartament(nr_apartament_id, lista):
    """
    Realizeaza suma totala a unui singur apartament la toate cheltuielile
    :param nr_apartament_id: numarul apartamentului
    :param lista: lista de dictionare
    :return: suma totala a cheltuielilor apartamentului
    """
    lista_noua = []
    suma_totala = 0
    for cheltuiala in lista:
        if get_nr_apartament_id(cheltuiala) == nr_apartament_id:
            lista_noua.append(cheltuiala)
    for apartament in lista_noua:
        suma_totala = suma_totala + get_suma(apartament)
    return suma_totala


def eliminare_cheltuieli_tip_cheltuiala(tip_cheltuiala, lista, undo_lista):
    """
    Elimina cheltuielile care au tipul de cheltuiala dat de la tastatura
    :param tip_cheltuiala: tipul de cheltuiala
    :param lista: lista de dictionare
    :return: lista de dictionare fara dictionarele care au acel tip de cheltuiala descris
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_tip_cheltuiala(cheltuiala) != tip_cheltuiala:
            lista_noua.append(cheltuiala)
    undo_lista.append(lista_noua)
    return lista_noua


def eliminare_cheltuieli_suma(suma, lista, undo_lista):
    """
    Elimina cheltuielile care au suma data la tastatura mai mica
    :param suma: suma data la tastatura
    :param lista: lista cu dictionare
    :return: lista cu dictionare noua
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_suma(cheltuiala) > suma:
            lista_noua.append(cheltuiala)
    undo_lista.append(lista_noua)
    return lista_noua


def undo(undo_lista):
    if len(undo_lista) > 0:
        return undo_lista.pop()
    else:
        return None

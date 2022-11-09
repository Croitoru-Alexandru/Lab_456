import datetime


def creeaza_cheltuiala(nr_apartament_id=int, suma=float, tip_cheltuiala=str, data=datetime):
    """
    Creeaza o cheltuiala a unui apartament
    :param data: data cand s-a realizat cheltuiala
    :param nr_apartament_id: Numarul apartamentului, id-ul - string
    :param suma: Cat este cheltuiala - float
    :param tip_cheltuiala: Descriere ( apa, curent, gaz, altele )
    :return: un dictionar ce retine cheltuiala apartamentului
    """
    return {
        'nr_apartament_id': nr_apartament_id,
        'suma': suma,
        'tip_cheltuiala': tip_cheltuiala,
        'data': data
    }


def get_nr_apartament_id(cheltuiala):
    """
    Preia nr. apartamentului
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: nr. apartamentului
    """
    return cheltuiala['nr_apartament_id']


def get_suma(cheltuiala):
    """
    Preia suma data
    :param cheltuiala:  dictionar de tipul cheltuiala
    :return: suma data
    """
    return cheltuiala['suma']


def get_tip_cheltuiala(cheltuiala):
    """
    Preia descrierea
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: descrierea
    """
    return cheltuiala['tip_cheltuiala']


def get_data(cheltuiala):
    """
    Preia data unei cheltuiele
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: data
    """
    return cheltuiala['data']


def to_string(cheltuiala):
    return f'Nr. apartament: {get_nr_apartament_id(cheltuiala)}, ' \
           f'Suma: {get_suma(cheltuiala)}, ' \
           f'Tip cheltuiala: {get_tip_cheltuiala(cheltuiala)}' \
           f'data: {get_data(cheltuiala)}'

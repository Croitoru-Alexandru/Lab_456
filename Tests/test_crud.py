from Domain.cheltuiala import get_nr_apartament_id, get_suma
from Logic.crud import adauga_cheltuiala, stergere_cheltuiala, \
    stergere_cheltuiala_tip, modifica_cheltuiala, get_by_id, \
    cautare_suma_mai_mare, cautare_cheltuiala_tip_cheltuiala, cautare_cheltuiala_data_suma, suma_totala_cheltuiala, \
    total_cheltuieli_apartament, eliminare_cheltuieli_tip_cheltuiala, eliminare_cheltuieli_suma


def test_adauga_cheltuiala():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (1999, 5, 14), lista, undo_lista)
    assert len(lista) == 1


def test_stergere_cheltuiala():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 200, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 340, 'curent', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 500, 'altele', (1999, 5, 14), lista, undo_lista)
    lista = stergere_cheltuiala(1, lista, undo_lista)
    assert len(lista) == 2


def test_modifica_cheltuiala():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (1999, 5, 14), lista, undo_lista)
    lista = modifica_cheltuiala(1, 750, 'altele', (1999, 5, 14), lista, undo_lista)
    assert len(lista) == 3
    assert get_nr_apartament_id(get_by_id(1, lista)) == 1
    assert get_suma(get_by_id(1, lista)) == 750


def test_stergere_cheltuiala_tip():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 200, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 340, 'curent', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 500, 'altele', (1999, 5, 14), lista, undo_lista)
    lista = stergere_cheltuiala_tip('gaz', lista, undo_lista)
    assert len(lista) == 4


def test_cautare_suma_mai_mare():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (2000, 6, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (2005, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 200, 'gaz', (2010, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 340, 'curent', (1995, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 500, 'altele', (1988, 5, 14), lista, undo_lista)
    lista = cautare_suma_mai_mare(200, lista)
    assert len(lista) == 3


def test_cautare_cheltuiala_tip_cheltuiala():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (2000, 6, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (2005, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 200, 'gaz', (2010, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 340, 'curent', (1995, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 500, 'altele', (1988, 5, 14), lista, undo_lista)
    lista = cautare_cheltuiala_tip_cheltuiala('gaz', lista)
    assert len(lista) == 2


def test_cautare_cheltuiala_data_suma():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (2000, 6, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (2005, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 200, 'gaz', (2010, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 340, 'curent', (1995, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 500, 'altele', (1988, 5, 14), lista, undo_lista)
    lista = cautare_cheltuiala_data_suma((1995, 5, 14), 200, lista)
    assert len(lista) == 1


def test_suma_totala_cheltuiala():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (2000, 6, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (2005, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 200, 'gaz', (2010, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 340, 'curent', (1995, 5, 14), lista, undo_lista)
    assert suma_totala_cheltuiala('gaz', lista) == 250
    assert suma_totala_cheltuiala('curent', lista) == 413


def test_total_cheltuieli_apartament():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (2000, 6, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (2005, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 200, 'gaz', (2010, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 340, 'curent', (1995, 5, 14), lista, undo_lista)
    assert total_cheltuieli_apartament(1, lista) == 774.5


def test_eliminare_cheltuieli_tip_cheltuiala():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (2000, 6, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (2005, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 200, 'gaz', (2010, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 340, 'curent', (1995, 5, 14), lista, undo_lista)
    assert len(eliminare_cheltuieli_tip_cheltuiala('gaz', lista, undo_lista)) == 3


def test_eliminare_cheltuieli_suma():
    lista = []
    undo_lista = []
    lista = adauga_cheltuiala(1, 234.5, 'apa', (2000, 6, 14), lista, undo_lista)
    lista = adauga_cheltuiala(2, 50, 'gaz', (1999, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(3, 73, 'curent', (2005, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 200, 'gaz', (2010, 5, 14), lista, undo_lista)
    lista = adauga_cheltuiala(1, 340, 'curent', (1995, 5, 14), lista, undo_lista)
    assert len(eliminare_cheltuieli_suma(100, lista, undo_lista)) == 3

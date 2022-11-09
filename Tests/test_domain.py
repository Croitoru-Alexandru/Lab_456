from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament_id, get_suma, get_tip_cheltuiala


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala('1', 273.5, 'Gaz')
    assert get_nr_apartament_id(cheltuiala) == '1'
    assert get_suma(cheltuiala) == 273.5
    assert get_tip_cheltuiala(cheltuiala) == 'Gaz'


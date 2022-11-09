from Tests.test_crud import test_adauga_cheltuiala, test_stergere_cheltuiala, test_modifica_cheltuiala, \
    test_stergere_cheltuiala_tip, test_cautare_suma_mai_mare, test_cautare_cheltuiala_tip_cheltuiala, \
    test_cautare_cheltuiala_data_suma, test_suma_totala_cheltuiala, test_total_cheltuieli_apartament, \
    test_eliminare_cheltuieli_tip_cheltuiala, test_eliminare_cheltuieli_suma
from Tests.test_domain import test_cheltuiala


def run_all_tests():
    test_adauga_cheltuiala()
    test_stergere_cheltuiala()
    test_modifica_cheltuiala()
    test_stergere_cheltuiala_tip()
    test_cheltuiala()
    test_cautare_suma_mai_mare()
    test_cautare_cheltuiala_tip_cheltuiala()
    test_cautare_cheltuiala_data_suma()
    test_suma_totala_cheltuiala()
    test_total_cheltuieli_apartament()
    test_eliminare_cheltuieli_tip_cheltuiala()
    test_eliminare_cheltuieli_suma()

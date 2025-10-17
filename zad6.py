'''Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz
średnie spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu
paliwa oraz o szacowanych kosztach podróży (cena paliwa 6.5 zł/l).

A) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo
(liczba całkowita z zakresu ), a użytkownik podawał aktualną cenę paliwa za litr.

B) Zmodyfikuj zadania 6 tak, aby wyświetlanie wyników wykorzystywało f-string.
'''
pokonana_droga=float(input("Podaj dlugosc pokonanej drogi:"))
średnie_spalanie=float(input("Podaj średnie spalanie samochodu (1/100km):"))
cena_paliwa_za_litr = 6.5

zużycie_paliwa= pokonana_droga * (średnie_spalanie / 100)
koszt_paliwa= zużycie_paliwa * cena_paliwa_za_litr

print("Zużycie paliwa wynosi:", round(zużycie_paliwa,2), "\nSzacowane koszta podróży:", round(koszt_paliwa,2))
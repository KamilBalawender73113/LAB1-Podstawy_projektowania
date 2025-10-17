'''Do zmiennej Cena przypisz cenę produktu równą 39.99 PLN oraz do zmiennej Rabat
przypisz wartość 0.2 (rabat 20%). Następnie policz cenę tego produktu po zastosowaniu
podanego rabatu. Wynik wydrukuj do konsoli. Zwróć uwagę na odpowiednie
formatowanie tekstu w funkcji print() tak, aby końcowa cena produktu została
wyświetlona tylko do drugiego miejsca po przecinku.
'''

cena= 33.99
rabat= 0.2

cena_po_rabacie=(cena - (cena * rabat))
print(round(cena_po_rabacie,2))
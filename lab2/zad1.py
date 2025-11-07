punkty = float(input("Podaj liczbę zdobytych punktów:"))
if punkty  > 80:
    print("Egzamin zdany")
elif punkty > 50:
    if punkty <80:
        print("Można poprawic (nieobowiązkowe)")
elif punkty < 50:
    print("Musisz poprawić egzamin")
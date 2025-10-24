print("Podaj współczynniki dla równania kwadratowego ax^2 + bx + c = 0:")
#Wczytywanie danych od użytkownika
a = float(input("Podaj a:"))
b = float(input("Podaj b:"))
c = float(input("Podaj c:"))

#Jeśli zmienna a równe zero - sprawdzamy zmienną b a następnie zmienną c
if a == 0:
    if b == 0:
        print("Brak rozwiązań")
    elif c != 0:
        print("Nieskończenie wiele rozwiązań")
    else:
        print(f"x={round(-c / b, 2)}")
else:
#W przypadku jeśli zmienna a jest różna od zera, liczymy deltę a następnie wynikające z niej miejsca zerowe
    delta = b ** 2 - 4 * a * c
    print(f"Delta wynosi {delta}")
    if delta > 0:
        x1= -b - delta **0.5 / 2*a
        x2= -b + delta **0.5 / 2*a
        print(f"x1 = {round(x1, 2)}")
        print(f"x2 = {round(x2, 2)}")
    elif delta == 0:
        print(f"x = {-b7 / (2 * a)}")
    elif delta < 0:
        print("Brak rozwiązań")
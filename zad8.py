print("Program rozwiązujący równanie kwadratowe ax^2 + bx + c = 0")
print("Podaj współczynniki dla równania kwadratowego ax^2 + bx + c = 0:")
#Wczytywanie danych od użytkownika
a = float(input("Podaj a:"))
b = float(input("Podaj b:"))
c = float(input("Podaj c:"))

#Jeśli zmienna a równe zero - sprawdzamy zmienną b a następnie zmienną c
if a == 0:
    if b == 0:
      if c == 0:
        print("Nieskończenie wiele rozwiązań")
      else:
        print("Brak rozwiązań")
    else:
        x = -c / b
        print(f"x wynosi: {round(x, 2)}")
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
        print(f"x wynosi: {round(-b / (2 * a),2)}")
    elif delta < 0:
        print("Brak rozwiązań")
    print("Wynik zaokrąglany do dwóch miejsc po przecinku")
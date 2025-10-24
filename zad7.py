print("Program rozwiązujący równanie liniowe ax + b = 0")

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

if a != 0:
    x = -b / a
    print(f"Rozwiązaniem równania jest x = {round(x, 2)}")
elif b == 0:
    print(f"Nieskończenie wiele rozwiązań")
else:
    print(f"Brak rozwiązań")
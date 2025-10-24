a = float(input("Podaj pierwszą liczbe: "))
b = float(input("Podaj drugą liczbe: "))

print("Wyniki działań:")
print(f"Dodawanie {a + b}")
print(f"Odejmowanie {a - b}")
print(f"Mnożenie {a * b}")

if b != 0:
    print(f"Dzielenie {round(a / b, 2)}")
else:
    print("Nie można dzielić przez 0")

print(f"Potęgowanie {a ** b}")
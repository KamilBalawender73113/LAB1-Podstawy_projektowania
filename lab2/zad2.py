x = float(input("Podaj liczbę x:"))
y = float(input("Podaj liczbę y:"))
z = float(input("Podaj liczbę z:"))

def zad2(x,y,z):
    if x>=y and x >=z:
        if y>=z:
            print(z,y,a)
        else:
            print(y,z,x)
    elif y>=x and y >=z:
        if z>=x:
            print(z,x,y)
        else:
            print(x,z,y)
    elif z>=x and z >= y:
        if x>=y:
            print(y,x,z)
        else:
            print(x,y,z)

print(zad2(x,y,z))
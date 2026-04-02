import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if a == 0:
    print("Não é equação de segundo grau")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não possui raízes reais")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Raiz única: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Raízes: {x1} e {x2}")
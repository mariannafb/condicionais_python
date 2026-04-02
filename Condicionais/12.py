li = int(input("Linha inicial: "))
ci = int(input("Coluna inicial: "))

lf = int(input("Linha final: "))
cf = int(input("Coluna final: "))

if not (1 <= li <= 8 and 1 <= ci <= 8 and 1 <= lf <= 8 and 1 <= cf <= 8):
    print("Posição inválida")
else:
    dl = abs(li - lf)
    dc = abs(ci - cf)

    if (dl == 2 and dc == 1) or (dl == 1 and dc == 2):
        print("Movimento válido")
    else:
        print("Movimento inválido")
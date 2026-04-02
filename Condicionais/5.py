vel = float(input("Velocidade do carro: "))
limite = float(input("Limite da via: "))

if limite <= 100:
    tolerancia = limite + 7
else:
    tolerancia = limite * 1.07

if vel <= tolerancia:
    print("Isento")
else:
    excesso = (vel - tolerancia) / limite

    if excesso <= 0.2:
        print("Multa Média")
    elif excesso <= 0.5:
        print("Multa Grave")
    else:
        print("Gravíssima + Suspensão")
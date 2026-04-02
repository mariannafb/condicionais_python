n = int(input("Número de 5 dígitos: "))

if n < 10000 or n > 99999:
    print("Número inválido")
else:
    d1 = n // 10000
    d2 = (n // 1000) % 10
    d4 = (n // 10) % 10
    d5 = n % 10

    if d1 == d5 and d2 == d4:
        print("Palíndromo")
    else:
        print("Não é palíndromo")
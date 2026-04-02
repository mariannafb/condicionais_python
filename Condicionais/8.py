valor = int(input("Valor: "))
if valor % 2 != 0:
    print("Valor impossível de sacar")
else:
    notas = [100, 50, 20, 10, 5, 2]
    for nota in notas:
        qtd = valor // nota
        if qtd > 0:
            print(f"{qtd} nota(s) de {nota}")
            valor %= nota
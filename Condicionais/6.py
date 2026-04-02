dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if ano < 1900 or ano > 2026:
    print("Ano inválido")
elif mes < 1 or mes > 12:
    print("Mês inválido")
else:
    dias_mes = [31, 29 if bissexto(ano) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if dia < 1 or dia > dias_mes[mes - 1]:
        print("Dia inválido")
    else:
        print("Data válida")
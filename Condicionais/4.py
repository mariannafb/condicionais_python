salario = float(input("Digite o salário bruto: "))

if salario <= 2000:
    imposto = 0
elif salario <= 4000:
    imposto = (salario - 2000) * 0.10
elif salario <= 8000:
    imposto = (2000 * 0.10) + (salario - 4000) * 0.20
else:
    imposto = (2000 * 0.10) + (4000 * 0.20) + (salario - 8000) * 0.30

liquido = salario - imposto

print(f"Salário bruto: R${salario:.2f}")
print(f"Imposto: R${imposto:.2f}")
print(f"Salário líquido: R${liquido:.2f}")
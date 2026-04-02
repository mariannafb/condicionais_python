peso = float(input("Peso: "))
regiao = input("Região: ").lower()
premium = input("Premium (True/False): ") == "True"

if regiao == "sudeste":
    valor = 10 + peso * 2
elif regiao == "sul":
    valor = 15 + peso * 3
elif regiao in ["norte", "nordeste"]:
    valor = 25 + peso * 5
elif regiao == "centro-oeste":
    valor = 20 + peso * 4
else:
    print("Região inválida")
    exit()

if peso > 20:
    valor += 30

if premium:
    valor *= 0.8

print(f"Frete: R${valor:.2f}")
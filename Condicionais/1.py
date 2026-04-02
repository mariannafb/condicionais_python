import math
h = float(input("Informe a altura (m): "))

G = -9.8

if h < 0:
    print("Altura inválida: a altura não pode ser negativa.")
else:
    t = math.sqrt((-2 * h) / G)
    print(f"O tempo de queda é {t:.2f} segundos.")
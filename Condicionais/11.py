# Retângulo 1
x1 = float(input("R1 x superior esquerdo: "))
y1 = float(input("R1 y superior esquerdo: "))
x2 = float(input("R1 x inferior direito: "))
y2 = float(input("R1 y inferior direito: "))

# Retângulo 2
x3 = float(input("R2 x superior esquerdo: "))
y3 = float(input("R2 y superior esquerdo: "))
x4 = float(input("R2 x inferior direito: "))
y4 = float(input("R2 y inferior direito: "))

if x1 > x4 or x3 > x2 or y1 < y4 or y3 < y2:
    print("Não se sobrepõem")
else:
    print("Se sobrepõem")
l1 = int(input("Informe o valor de l1: "))
l2 = int(input("Informe o valor de l2: "))
l3 = int(input("Informe o valor de l3: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:

    if l1 == l2 == l3:
        print("Triângulo equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo Isósceles.")
    else:
        print("Triângulo escaleno.")

    if (pow(l1,2) + pow(l2,2) == pow(l3,2)) or (pow(l1,2) + pow(l3,2) == pow(l2,2)) or (pow(l2,2) + pow(l3,2) == pow(l1,2)):
        print("Triângulo retângulo.")
    else:
        print("Triângulo comum.")
else:
    print("Valores inválidos, não formam um triângulo.")
import math
xc = float(input("Centro x: "))
yc = float(input("Centro y: "))
r = float(input("Raio: "))
x = float(input("Ponto x: "))
y = float(input("Ponto y: "))

dist = math.sqrt((x - xc)**2 + (y - yc)**2)

if dist < r:
    print("Dentro")
elif dist == r:
    print("Na borda")
else:
    print("Fora")
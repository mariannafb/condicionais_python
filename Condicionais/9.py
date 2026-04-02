hi = int(input("Hora inicial: "))
mi = int(input("Min inicial: "))
hf = int(input("Hora final: "))
mf = int(input("Min final: "))
inicio = hi * 60 + mi
fim = hf * 60 + mf
if fim <= inicio:
    fim += 24 * 60
duracao = fim - inicio
horas = duracao // 60
minutos = duracao % 60
print(f"O jogo durou {horas} hora(s) e {minutos} minuto(s)")
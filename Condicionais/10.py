senha = input("Senha: ")
if len(senha) < 8:
    print("Inválida")
elif senha.islower() or senha.isdigit():
    print("Fraca")
elif senha.isalnum():
    print("Média")
else:
    print("Forte")
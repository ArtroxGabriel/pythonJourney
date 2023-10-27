import string
import random

def generator():
    print("""
    ++====================++
    ||                    ||
    || Password Generator ||
    ||                    ||
    ++====================++
""")
    quant = int(input("Quantas senhas voce deseja gerar? "))
    tam = int(input("Insira o tamanho das senhas: "))

    chars = string.ascii_lowercase + string.digits

    escolhas = input("\nSua senha deve ter letra maiuscula?\n Digite 's' para confirmar ")
    if escolhas.lower() == 's':
        chars += string.ascii_uppercase

    escolhas = input("\nSua senha deve ter caracteres especiais??\n Digite 's' para confirmar ")
    if escolhas.lower() == 's':
        chars += string.punctuation

    print(f"\n Sua senha de {tam} digitos está aqui:")
    for pwd in range(quant):
        passwords = ''

        for c in range(tam):
            passwords += random.choice(chars)
        print(f"\t{passwords}\n")



generator()
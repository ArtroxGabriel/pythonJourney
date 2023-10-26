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
    quant = int(input("Quantas senhas voce deseja gerar?"))
    tam = int(input("Ensira o tamanho das senhas"))

    chars = string.printable
    print(chars)



generator()
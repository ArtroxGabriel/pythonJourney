import random
"""Busca binária em uma lista ordenada."""
def bylist(list, x, inicio, fim):
    # caso base: list vazia
    if inicio > fim:
        return None

    meio = (inicio + fim) // 2

    if list[meio] == x:
        return meio

    if list[meio] > x:
        return bylist(list, x, inicio, meio - 1)
    return bylist(list, x, meio + 1, fim)

lista = [i**3 for i in range(10000)]


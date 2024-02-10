numeros = input("Ingresa los numeros a ordenar (Separados por espacios):\t")
listaNumeros = [x for x in numeros.split()]


listaNumeros.sort()
print(listaNumeros)
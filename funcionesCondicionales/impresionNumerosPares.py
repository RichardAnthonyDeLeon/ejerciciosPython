
print('Los primeros 10 números pares empezando desde el cero son: ')
numeros = []
num = 0
while num < 21:
    numeros.append(num)    
    num += 1

for x in numeros:
    if(x%2 == 0):
        print(x)
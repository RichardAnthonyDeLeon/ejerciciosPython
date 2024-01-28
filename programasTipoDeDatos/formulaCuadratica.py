<<<<<<< HEAD
import math 

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

bNegativo = -b
bCuadrado = b**2
cuatroAc = 4*a*c

interiorRaiz = bCuadrado - cuatroAc

discriminante = math.sqrt(interiorRaiz)

numerador1 =  bNegativo + discriminante

denominador = 2*a


resultado1 = numerador1/denominador



numerador2 = bNegativo - discriminante

resultado2 = numerador2/denominador


=======
import math 

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

bNegativo = -b
bCuadrado = b**2
cuatroAc = 4*a*c

interiorRaiz = bCuadrado - cuatroAc

discriminante = math.sqrt(interiorRaiz)

numerador1 =  bNegativo + discriminante

denominador = 2*a


resultado1 = numerador1/denominador



numerador2 = bNegativo - discriminante

resultado2 = numerador2/denominador


>>>>>>> 10dc2c0336c4eaa1dc61ad55d8a7e288f9063b0f
print("Resultado 1 =",resultado1,"\n","Resultado 2 =",resultado2)
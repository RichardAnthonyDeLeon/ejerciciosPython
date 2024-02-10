
print('\nConversión de kilómetros a millas**********\n')
def conversion(kilometros):
    millaEnKm = 0.621371
    return kilometros * millaEnKm


try: 
    kms = float(input("Ingresa los Kilometros: "))
    millas = round(conversion(kms),2)
    mensaje = f"{kms} kilometros son: {millas} Millas'"
    print(mensaje)
    
except ValueError:
    print('¡Error! Por Favor Ingresa un numero')
    
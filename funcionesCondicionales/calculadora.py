

def suma(num1,num2):
    res = round(num1 + num2,2)
    print('La Suma es:',res)

def resta(num1,num2):
    res = round(num1 - num2,2)
    print('La Resta es:',res)

def multi(num1,num2):
    res = round(num1 * num2,2)
    print('La Multiplicación es:',res)
    
def division(num1,num2):
    res = (num1 *100 // num2)/100
    print('La División es:',res)


try: 
    num1 = float(input('Ingresa el primer número: '))
    num2 = float(input('Ingresa el segundo número: '))
    suma(num1,num2)
    resta(num1,num2)
    multi(num1,num2)
    division(num1,num2)
except ValueError:
    print('Tienes que ingresar Números! ')
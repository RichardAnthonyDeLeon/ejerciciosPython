

try:
    num = float(input('Ingrese un número: '))
    
    if(num > 0):
        print('El número ingresado es positivo')
    elif(num < 0):
        print('El número ingresado es negativo')
    elif(num==0):
        print('El número es 0')
        
except ValueError:
    print('Ingresa un número!') 
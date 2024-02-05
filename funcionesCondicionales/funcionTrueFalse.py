

def parImpar(num1,num2):
    suma = num1 + num2
    residuo = suma % 2
    
    if(residuo == 0):
        print(f'TRUE! El resultado de la suma es {suma} y es un número par')
    else:
        print(f'FALSE! El resulatdo de la suma es {suma} y es un número impar')
        
try:
    num1 = float(input('Ingrese el primer número: '))
    num2 = float(input('Ingrese el segundo número: '))
    parImpar(num1,num2)
    
except ValueError:
    print('Ingres números! ')
# dato = input('Ingrese dato: ')
# #print(dato)

# lista = ['toby', 'many', 'reina', 'canela', 'docky']
# if lista.count(dato) > 0:
#     print('El dato existe:', dato)
# else:
#     print('El dato no existe:', dato)

# primero = input('Ingrese primer numero: ')
# segundo = input('Ingrese segundo numero: ')
# primerNum = int(primero)
# segundoNum = int(segundo)
# #int() transforma los string en numeros enteros
# print(primerNum + segundoNum)

primero = input('Ingrese primer numero: ')

try: 
    primero = int(primero)
except:
    primero = 'cerdaquito feliz'

if primero == 'cerdaquito feliz':
   print('El valor ingresado no es un entero')
   exit()

segundo = input('Ingrese segundo numero: ')

try:
    segundo = int(segundo)
except: 
    segundo = 'cerdaquito feliz'

if segundo == 'cerdaquito feliz':
   print('El valor ingresado no es un entero')
   exit()

#if primero == 'cerdaquito  feliz' or segundo == 'cerdaquito feliz':
#    print('Ingresaste mal un dato, prueba de nuevo solo con numeros enteros')
#else:

simbolo = input('Ingrese operacion: ')

if simbolo == '+':
   print('Suma: ', primero + segundo)

elif simbolo == '-':
    print('Resta: ', primero - segundo)
elif simbolo == '/':
    print('Division: ', primero / segundo)
elif simbolo == '*':
    print('Multiplicacion: ', primero * segundo)
else:
    print('El simbolo ingresado no es valido')
    
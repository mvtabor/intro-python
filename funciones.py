# == FUNCIONES== : Bloques de codigo que no se ejecutana menos que se le llame; pueden reutilizar codigos que ya hemos escrito.

def miFuncion(): #def palabra reservada, nombre y cierra con ():
    print('Mi primera funcion!') #logica que queremos que ejecute la funcion.

#miFuncion()  #se llama a la funcion para que ejecute lo definido en el bloque anterior

# def imprimeDato(nombre):
#     print('Mi nombre completo es', nombre)

# imprimeDato('Cerdaquito')

def imprimeDato(*nombre): #* indica que podemos dar un numero de datos variables, puede recibir más de un argumento, como una lista
    print('Mi nombre completo es', nombre[0])

#imprimeDato('Cerdaquito', 'feliz', 'programador', 'rosadito')
#imprime como tupla y no podemos modificarlo, [---] nos ayuda a indicar la posicion del elemento al que queremos acceder

def nombreComp(apellido , nombre):
    print(nombre, apellido)

#nombreComp(nombre='Chancho', apellido='libre')
def karlucha(*animos):
    for animo in animos:
        print('Karlucha esta', animo)

#karlucha('feliz', 'horny', 'hambrienta', 'triste', 'comiendo', 'sonriendo')


def nombreComp2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

#nombreComp2(nombre='Chancho', apellido='libre')

def funcion(argumento1, argumento2, *args, **kwards):
    print(argumento1, argumento2, args[0], kwards['actividad'])

#funcion('Karla', 'esta', 'caliente y', 'enojada y', 'contenta y', 'soñolienta y', actividad='con ganas de salir')

# argumento = parametro
# *args = numero indeterminado de argumentos
# **kwargs = argumento por llave para acceder con la sintaxis de los diccionarios

def miFun1(**pets):
    for key, value in pets.items():
        print(f"{key}: {value}")

#miFun1(name="doky", raza="chihua")

def miFun2(*args, **kwargs):
     for arg in args:
         print(arg)
     for key, value in kwargs.items():
         print(f"{key}: {value}")

#miFun2(1,2, nombre="Luis", age=32)


def miFuncion2( argumento = 'cerdaquito'): 
    print(argumento) 
    #valor por defecto del argumento, de manera que si no se le asigna parametro a la funcion
    #

#miFuncion2('berraquito')
#miFuncion2()
#miFuncion2('Batman')

def miFuncLista(lista):
    for elemento in lista:
        print(elemento)

#miFuncLista(['cerdaquito', 'berraquito', 'cochi'])
#le podemos pasar una lista como argumento

def concateNombres(lista):
    i = ' ' #variable vacia
    for elem in lista:
        i = i + elem + ' ' #o bien i= i + ' ' + elem : igual a mismo i mas espacio mas elemento concatenado
    return i

names = concateNombres(['cerdaquito', 'berraquito', 'feliz'])
#print(names)

def recursion(i):
    if(i < 1):
        return i
    print(i) 
    recursion(i - 1)

recursion(9)

#cuando utilizamos recursividad escribimos la logica a utilzar y una condicion de salida
# si se cumple la condicion detenemos la ejecucion de esta funcion
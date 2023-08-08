#PRIMER EJERCICIO: multiplicar dos números sin usar el símbolo de multiplicación
print('Multiplicar dos numeros sin usar el simbolo de multiplicacion') #sólo para ver la leyenda en la terminal de GitBash 
a = 7 #declaramos variable a y b. 
b = 8
resultado = 0 #declaramos resultado empezando en 0.

for x in range(a):  #Se empieza a iterar una cantidad de veces determinada -ya sea por el primero o segundo- a o b, y se suma el otro valor.
    resultado += b # resultado = resultado + b ; #o sea, si se itera 4 (range a), se suma 8 tantas veces como el range lo indique.
print(resultado)

#Ahora un método en el que se ingresen valores

#num1 = input('Ingrese el primer valor:')
#val1 = int(num1) #int convierte el string en entero

#num2 = input('Ingrese el segundo valor:')
#val2 = int(num2)

#i = 0 #inicia del contador que es el numero de veces que se sumará val1
#res = 0 #inicializa la variable que tendrá el resultado
#while i < val2:
#    res += val1
#    i += 1

#print(val1, '*', val2, '=', res)


#SEGUNDO EJERCICIO: ingresar nombre y apellido e imprimirlo al reves


name = 'Luis'
lastn = 'Angulo'
concatenacion = name + ' ' + lastn
print(concatenacion[::-1]) # [::-1] notación de Slice: con esta operación podemos dar vuelta a un string ya que no existe una función. Dicha función
#comienza del final hacia el principio tomando cada elemento. Se invierte, es aplicable a listas y tuplas. 

#nombre = input('Ingrese nombre:')
#apellido = input('Ingrese apellido:')
#nomCompleto = nombre + ' ' + apellido
#print(nomCompleto[::-1])

#TERCER EJERCICIO: escribir una funcion que encuentre el elemento menor de una lista

lista = [1,2,3,55,-24,-13,18,0,9]
menor = 'init' #generamos un valor inicial
#Reservo el 1er elemento, lo comparo con el 2do; si éste es menor que el 1ro, mantengo el 2do y salto al siguiente.
for x in lista: #iterar lista
    if menor == 'init': #preguntamos si menor es igual a 'init'; si es igual no tenemos reservado el primer número y estamos en la primera iteración
        menor = x #menor es igual a x, o sea, igual a 1 en la lista 
    else:
        menor = x if x < menor else menor #si no es así, menor = x siempre que x sea tenga menos valor que menor (menor = x if x < menor); si no es así (else),
        #a menor se le sigue asignando el valor de menor, o sea que su valor no cambia

print('menor valor en lista es:', menor)

#CUARTO EJERCICIO: escribe una funcion que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r **3

def calVolumen(r):
    return (4/3) * 3.1416 * (r ** 3) #arroja el mismo resultado si se escribe en paréntesis o no 4/3 * pi * r **3

res = calVolumen(9)
print(res)

#QUINTO EJERCICIO: escribir una funcion que indique si un usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad > 17 #devuelve un booleano True o False

class Usuario: #creamos la clase de usuario
    def __init__(self, edad): #le asignamos la propiedad de edad
        self.edad = edad

usuario1 = Usuario(15) #creamos instancias de usuario
usuario2 = Usuario(21)
usuario3 = Usuario(24)

resultado1 = esMayor(usuario1) #llamamos la funcion de esMayor() con los usuarios
resultado2 = esMayor(usuario2)
resultado3 = esMayor(usuario3)

print(resultado1, resultado2, resultado3)

#SEXTO EJERCICIO: escribir una función que indique si un numero es par o impar

def esPar(n):    # operador módulo % nos indique si hay un residuo al dividir un numero entre otro. Ejemplo: 10 % 2 = 0; 5 % 2 = 1
    return n % 2 == 0 #realizamos la operación módulo (%) con 2, igual a 0 para saber si es par.

resultado = esPar(10)
resultado4 = esPar(9)

#print(resultado, resultado4)

#SEPTIMO EJERCICIO: escribir una funcion que indique cuaántas vocales tiene un string (palabra)

palabra = 'OnTheMoveALife' #palabra a leer (libre de Oliver Sacks)
vocales = 0 #variable con valor inical 0

for x in palabra: #iteramos sobre cada letra
    y = x.lower() # el método de .lower() evalua si el string está en mayúscula y lo tranforma a minuscula 
    vocales += 1 if y == 'a' or y == 'e' or y =='i' or y =='o' or y == 'u' else 0

#print(vocales)

#OCTAVO EJERCICIO: escribir una aplicación que reciba una cantidadde números hasta decir basta, luego que devuelva la suma de los datos ingresados.

# lista = [] #construimos lista donde se almacenarán los datos ingresados
# print('Ingrese numero o escriba "basta" para salir: ')
# while True:   #indicamos que hay que iterar hasta que se cumpla una condicion de salida.
#     valor = input('Ingrese valor: ')  #le pedimos un valor al usuario.
#     if valor == 'basta':  #si el valor es basta, entonces rompemos con el loop.
#         break
#     else:  #no ser no romper el loop, intentamos lo siguiente con el valor ingresado:
#         try:
#             valor = int(valor) #transformar el string (numero) a entero
#             lista.append(valor) #lo agregamos a la lista
#         except: #de no ser un dato válido
#             print('Dato invalido')
#             exit() #salimos del programa

# resultado = 0 #siempre iniciamos con 0 para no afectar el resultado final
# for x in lista: #iterando los valores ingresados
#     resultado += x #sumando valores

# print(resultado) 

#NOVENO EJERCICIO: escribir una función que reciba nombre y apellido y los vaya agregando a un archivo

def agregNombreArchivo(nombre, apellido):
    c = open('nombreCompleto.txt', 'a') #creamos el archivo, asignando el permiso 'a' para ir agregando datos.
    c.write(nombre + ' ' + apellido + '\n') #pasamos nombre y apellido debidamente concatenado y con la instrucción '\n' para que los agregue en una nueva línea
    c.close() #cerramos archivo

agregNombreArchivo('Luis', 'Angulo')
agregNombreArchivo('Karla', 'Molanz')
agregNombreArchivo('Greta', 'MA')
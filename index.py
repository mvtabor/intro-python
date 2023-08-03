# comentario
if 3 > 5:
    print('Esto no se imprime')

#if 5 > 3: 
#    print('5 es mayor a 3')

x = 5
y = 'chanchito feliz'

print(x,y)

correo = 'chancho@feliz.com'
print (correo)

mi_var = 'chanchito'

#multiples variables

a, b, c = 'Lala', 'Lele', 'Lili'
#print(a,b,c)

#para darle el mismo valor a las variables
valor1 = valor2 = valor3 = 'chanchito feliz'
#print(valor1, valor2, valor3)

#concatenacion ('variable' + 'variable'); distinto a usar la coma que muestra un espacio

inicio = 'Hola '
final = 'mundo'

#print(inicio + final)

#TIPOS DE DATOS

#string = palabra o frase u oracion en comillas simples o dobles '', ""

palabra = 'hola mundo' #string
oracion = "hola mundo comilla doble" #string

entero = 20 #integer
conDecimales = 20.2 # float
numComplejo = 1j #comlejo, se le agrega la j

#print(palabra, oracion, entero, conDecimales, numComplejo)

#==LISTA==: coleccion de datos o datos agrupados

lista = ['hola', 'mundo', 'chanchito feliz']
lista2 = lista.copy()
lista.append('chancho triste') #.append() para agregar elementos a la lista
#lista.clear()  #.clear() elimina los elementos de la lista 
#.count() contar un elemto en lista y ver cuantas veces se repite

#print(lista, lista2.count(3))
#print(len(lista), len(lista2)) #len() cuenta elementos en lista
largolista = len(lista)
largolista2 = len(lista2)

#print(largolista, largolista2)
#print(lista[2]) #[] accediendo a un elemento en lista

#para acceder a un elemtos, hay que pensar en en el indice, y siempre inicia con 0,
#no hay que pensar en la posicion en la lista

#lista.pop() #.pop() elimina ultimo elemento de la lista
#lista.pop()

#lista.remove('mundo') #.remove() elimina elemento en particular

lista.reverse() #.reverse() ambia el orden al reves
lista.sort() #.sort() ordena una lista con un mismo tipo de dato; string o entero
#print(lista)

#==TUPLAS== : no son modificables como las litas

tupla = ('hola', 'mundo', 'somos', 'tupla', 'canada')
#print(tupla.count('canada'))
#print(tupla.index('canada')) #.index() nos dice la posicion donde encontro un elemento
#print(tupla[2])
listaDeTupla = list(tupla)
listaDeTupla.append('chancho')
#print(listaDeTupla)

rango = range(6) #range() rango indicado de elementos
#print(rango)

#==DICCIONARIOS==  se utilizan strings para referirse a un valor
# se define con llaves {}
diccionario = {
    "nombre": "pascual",
    "raza": "dalmata",
    "edad": 5
}

#print(diccionario)
#print(diccionario['raza'])
#print(diccionario['nombre'])
#print(diccionario.get('nombre')) #.get() para acceder a valores especificos sin usar corchetes []

diccionario['nombre'] = 'Luffy' #cambiar valores

#print(len(diccionario))

diccionario['ronronea'] = 'si' #agregar valor al diccionario

#print(diccionario)
#diccionario.pop('raza') #.pop() indicas el valor a eliminar
#diccionario.popitem() #.popitem elimina el ultimo valor agregado

#copiaPerrito = diccionario.copy()
copiaPerrito = dict(diccionario) #dict() es otra forma de hacer una copia
#del diccionario['ronronea'] #del es otra manera de eliminar un valor agregado
diccionario.clear()
#print(diccionario, copiaPerrito)

#lomitos = {  #diccionarios anidados, un diccionario dentro de otro
#    "toby": {
#        "nombre": "Toby",
#        "edad": 9
#    },
#    "pairus":{
#        "nombre": "Pairus",
#        "edad": 2
#    }
#}

toby = {
    "nombre": "Toby",
    "edad": 9
}

pairus = {
    "nombre": "pairus",
    "edad": 2
}

lomitos = {
    "toby" : toby,
    "pairus" : pairus
}

print(lomitos)

gatitos = dict(nombre ="misho", edad = 3, raza = "gato naranja")
print(gatitos)

#==BOOLEANOS== : verdadero o falso

verdadero = True
falso = False

print(verdadero, falso)

#CONTROL DE FLUJO: ver decisiones qué podemos tomar en el camino y ver qué camino elegir

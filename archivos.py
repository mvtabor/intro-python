#c = open('toby.txt') #open nos permite abrir un archivo especificando donde se encuentra o utilizando el nombre
#c = open('toby.txt', 'read', 'a', 'w', 'x') #permisos: read implicito; append = a; write = w; x crear archivo en caso de que no exista.
#print(c.read()) #nos permite leer la totalidad del archivo
# print(c.readline())
# print(c.readline()) #.readline() leerá el archivo linea por linea
# print(c.readline()) 
# print(c.readline()) 
# print(c.readline())
# print(c.readline()) 
# print(c.readline())

# append : si queremos modificar el archivo, agregando texto
#write : si queremos modificar el archivo completamente

#for x in c:  #tenemos un control más específico por cada una de las lineas sin escribir muhco .readline
#    print(x)

#c.close() #por buena pratica, cerramos el archivo con este método

# c = open('toby.txt', 'w')

# c.write('\nagregamos una nueva linea al archivo txt') #\n agregamos una nueva linea al archivo txt = \ ALT GR + tecla de ?'\ (past 0)
# c.close()

# x = open('toby.txt')
# print(x.read())

#si utilizamos el permiso de write 'w', elininará los datos del archivo ya que busca modificar completamente el archivo. En este ajemplo sólo
#imprime lo agregado en la linea 22.
#Si lo que queremos es agregar una linea, sólo utilizar el permiso de append y no write.


import os # para eliminar archivos, vamor a importar esta libreria -os-, 
if os.path.exists('toby.txt'): #validamos si existe el archivo con este mismo modulo de os
    os.remove('toby.txt') #con el metodo de .remove eliminamos el archivo
else:
    print('El archivo no existe')

os.rmdir('micarpeta') #eliminar directorios o carpetas
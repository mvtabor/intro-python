#i = 0

# while i < 5:
#     print(i)
#     #i = i + 1
#     if i == 3:
#         break
#     i += 1

# while i < 5:
#     i += 1
#     if i ==3:
#         continue
#     print(i)

# usuarios = ['Mollis', 'Key', 'Homero', 'Oscar', 'Chelo']

# for usuario in usuarios:
#     print(usuario)

#for loop para accerder a los elementos de una lista

# usuario = 'Cerdaquito feliz'

# for c in usuario:
#     print(c)

# usuarios = ['Mollis', 'Key', 'Homero', 'Oscar', 'Chelo']

# for usuario in usuarios:
#      if usuario == 'Homero':
#           break
#      print(usuario)

# usuarios = ['Mollis', 'Key', 'Homero', 'Oscar', 'Chelo']

# for usuario in usuarios:
#      if usuario == 'Homero':
#           continue
#      print(usuario)

#for x in range(9):
#    print(x)


#for x in range(2,8): #podemos manipular range indicandole cual sera el valor inicial
#    print(x)         #pasandoselo en el primer valor

#for x in range(2, 30, 4): #el tercer valor indica de cuanto ira aumentando el conteo
 #   print(x)
#else:
 #   print('Hemos terminado') #en los for loops, else se ejecuta al terminar de iterar todos los elementos

usuarios = ['Mollis', 'Key', 'Homero', 'Oscar', 'Chelo']
edaddes = [29, 28, 30, 32, 31]

for usuario in usuarios:
    for edad in edaddes:
        print(usuario, edad)



#CONTROL DE FLUJO: ver decisiones qué podemos tomar en el camino y ver qué camino elegir
# if 2 < 5:
#     print('2 es menor que 5')
# a ==
# a < b
# a > b
# a != b (!= distinta)
# a <= b
# a >= b

# if 2 == 2:
#     print('2 es igual a 2')
# if 2 == 3:
#     print('2 es igual a 3')
# if 2 > 5:
#     print('2 es mayor a 5')
# if 5 > 2:
#     print('5 es mayor a 2')
# if 2 != 2:
#     print('2 es distinto a 2')
# if 3 != 2:
#     print('3 es distinto a 2')
# if 3 >= 2:
#     print('3 es mayor o igual a 2')
# if 3 >= 3:
#     print('3 es mayor o igual a 3')

#if 2 > 5:
#    print('lala')
#elif 2 < 5: #elif si if evalua negatigo, se evalua elif
#    print('2 es menor a 5 en elif')

if 2 > 5:
    print('2 es menor a 5 en if')
elif 2 > 5: #elif si if evalua negatigo, se evalua elif
    print('2 es mayor a 5 en elif')
elif 4 < 5:
    print('4 es mmenor a 5 en segundo elif')
#si la condicion se cumple en if, incluso si elif es verdadera no se va a ejecutar
else:
    print('yo me imprimo solo si todo if y elif evalua en falso')

if 2 > 5:
    print('2 es mayor a 5 en if')
else:
    print('yo me imprimo solo si todo if y elif evalua en falso 2')

if 2 < 5: print('if de una linea')
#OPERADOR TERNARIO: if de una linea y else por si evalua en falso
print('cuando devuelve True') if 2 > 5 else print('cuando devuelve False')


if 2 < 5 and 3 > 2:
    print('ambas devuelven True')
#and sirve para dar más de una condicon y se ejecuta solo cuando ambas devuelven true.

if 3 < 1 or 3 > 1:
    print('uno de los dos devuelve True')
#si if es True, todo es true. Si False, evalua la siguiende condion como True.
if 3 < 1 or 3 < 1:
    print('si ambos false no imprime')
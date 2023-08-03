# from modulos import saludo, mascotas  #from palabra reservada para extraer solo un elemento

# print(mascotas)
# saludo('Luis')

import modulos as xs #palabra reservada import seguido del archivo deseado; as para renombrar 
from camelcase import CamelCase

print(xs.mascotas) #importamos lista
xs.saludo('Luis')  #importamos la funcion

c = CamelCase()
s = 'Esta oración necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)


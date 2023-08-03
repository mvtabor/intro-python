#class Usuario: #por convencionalismo, al crear una clase se utiliza mayuscula la primera letra
    #nombre = 'Felipe'
    #apellido = 'Solis'
    #mote = 'Pipe'
#   def __init__(self, nombre, apellido, mote): #__init__ se ejecuta siempre que creamos instancias de estas clases 
#    self.nombre = nombre  #self hace referencia del objeto cuando lo instanciamos; sirve para crear objetos con valores distintos
#    self.apellido = apellido
#    self.mote = mote

   
# usuario = Usuario('Felipe', 'Solis', 'Pipe') #las instancias con minuscula
# usuario2 = Usuario('Carlos', 'Coronel', 'Talo')
# print(usuario.nombre, usuario.apellido, usuario.mote, usuario2.nombre, usuario2.apellido, usuario2.mote) #.nombre para acceder a la propiedad
#print(usuario.apellido)
#print(usuario.mote)

#Las clases son el plano de lo que queremos crear y los objetos son las instancias de los planos.

class Usuario:
   def __init__(self, nombre, apellido, mote):
     self.nombre = nombre
     self.apellido = apellido
     self.mote = mote

   def saludo(self):
     print('Hola, mi nombre es', self.nombre, self.apellido, 'y me dicen', self.mote)

class Admin(Usuario):
  def superSaludo(self):
    print('Hola, me llamo', self.nombre, 'y soy Administrador')

# usuario = Usuario('Felipe', 'Solis', 'Pipe')
# usuario2 = Usuario('Carlos', 'Coronel', 'Talo')
# usuario.saludo()
# usuario2.saludo()


# class Usuario:
#   def __init__(self, nombre, apellido, mote):
#     self.nombre = nombre
#     self.apellido = apellido
#     self.mote = mote

#   def saludo(lala):
#     print('Hola, mi nombre es', lala.nombre, lala.apellido, 'y me dicen', lala.mote)

#usuario = Usuario('Felipe', 'Solis', 'Pipe')
#usuario2 = Usuario('Carlos', 'Coronel', 'Talo')
#usuario.saludo()
#usuario2.saludo()

#no tiene que ser necesariamente self, pero por buena practica se le da el nombre a ese argumento para una buena lectura del codigo

#usuario.nombre = 'Cerdaquito' #podemos cambiar las propiedades de las instancias
#usuario.saludo()
#admi = Admin('Karla', 'Molanz', 'Karlucha')
#admi.saludo()
#admi.superSaludo()

#del usuario.nombre #podemos eliminar propiedades
#usuario.saludo()
#del usuario #podemos eliminar un usuario por completo
#print(usuario)

class Animal:
 def __init__(self, nombre, onomatopeya):
    self.nombre = nombre
    self.onomatopeya = onomatopeya

 def saludo(self):
   print('Hola, soy un', self.animal, ', mi nombre es', self.nombre, 'y mi sonido es el', self.onomatopeya) 


class Gato(Animal):
    animal = 'gatico'
    def __init__(self, nombre, onomatopeya): #extendemos el metodo de __init__ igual que en la clase padre; aqui ignora la clase padre
       Animal.__init__(self, nombre, onomatopeya) #para que se indique que se ejecute de todas maneras se hace ref a la clase padre y llamar a __init__ con los argumentos y self
       print('Hola, soy un gatico extendido!') #para demostrar que se extiende el comportamiento del metodo
  #  self.nombre = nombre
  #  self.onomatopeya = onomatopeya

  #def saludo(self):
   #print('Hola, soy un', self.animal, ', mi nombre es', self.nombre, 'y mi sonido es el', self.onomatopeya)

class Perro(Animal):
    animal = 'lomito'
    def __init__(self, nombre, onomatopeya):
       super().__init__(nombre, onomatopeya) #super hace ref a la clase padre y no es necesario pasarle la ref de la instancia (self)
       print('Instanciando un perro!')
  #  self.nombre = nombre
  #  self.onomatopeya = onomatopeya

  #def saludo(self):
  #  print('Hola, soy un', self.animal, ', mi nombre es', self.nombre, 'y mi sonido es el', self.onomatopeya)

class Loro(Animal):
   animal = 'loro'

gato = Gato('Pichirilo', 'maullido')
gato.saludo()
perro = Perro('Tobiropo', 'ladrido')
perro.saludo()
ave = Loro('Lencho', 'garren')
ave.saludo()

#el comun denominador que es el metodo de __init__ se toma y se lleva a otra clase, que eventualmente heredara el metodo

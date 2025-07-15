##Crea una clase Tarta que permita almacenar el sabor y una puntuación 
##Puedes comprobar si una tarta te gusta más que otra comparando los valores de sus atributos puntuacion.

class Tarta():
    sabor = ""
    puntuacion = 0
    
    def __init__(self, sabor):
        self.sabor = sabor
        
        
manzana = Tarta('manzana')
manzana.sabor
manzana.puntuacion = int(input('Puntua la tarta de manzana del 1 al 5: '))
if manzana.puntuacion < 0 or manzana.puntuacion> 5:
    print("Error: Puntuación no válida.")
    exit()

chocolate = Tarta('chocolate')
chocolate.sabor
chocolate.puntuacion = int(input('Puntua la tarta de cholocolate del 1 al 5: '))
if chocolate.puntuacion < 0 or chocolate.puntuacion> 5:
    print("Error: Puntuación no válida.")
    exit()

if chocolate.puntuacion > manzana.puntuacion:
    print('La tarta de chocolate es la que más me gusta')
else:
    print('La tarta de manzana es la que más me gusta')
'''
##Crea un programa para llevar la cuenta de las series y películas que has visto
#1.Define una clase Show que permita crear cada una de ellas. La clase debe tener los siguientes atributos:
titulo,tipo(film, serie, doc), terminada(True or False), fecha_entrada(se rellena automáticamente con la fecha del día)
#2.Crea un objeto para cada elemento y agrégalo a una lista llamada mis_pelis
#3.Recorre la lista mis_pelis e imprime cada objeto en una línea por la consola. 
'''


from datetime import date

class Show:
    
    def __init__(self, titulo, tipo):
        self.titulo = titulo
        self.tipo = tipo
        self.fecha = date.today()
        
    def __str__(self):
        return f"Titulo: {self.titulo} \tTipo: {self.tipo} \tTerminada: {self.terminada} \tFecha: {self.fecha}"
        
        
mis_pelis = []

peli_starwars = Show('Star Wars', 'film')
mis_pelis.append(peli_starwars)
peli_starwars.terminada = input('¿Has terminado de ver Star Wars? (s/n): ')
if peli_starwars.terminada == 's':
    peli_starwars.terminada = True
else:
    peli_starwars.terminada = False


peli_avatar = Show('Avatar 2', 'film')
mis_pelis.append(peli_avatar)
peli_avatar.terminada = input('¿Has terminado de ver Avatar 2? (s/n): ')
if peli_avatar.terminada == 's':
    peli_avatar.terminada = True
else:
    peli_avatar.terminada = False


docu_worm = Show('Wormwood', 'doc')
mis_pelis.append(docu_worm)
docu_worm.terminada = input('¿Has terminado de ver Wormwood? (s/n): ')
if docu_worm.terminada == 's':
    docu_worm.terminada = True
else:
    docu_worm.terminada = False


serie_wire = Show('The Wire', 'serie')
mis_pelis.append(serie_wire)
serie_wire.terminada = input('¿Has terminado de ver The Wire (s/n): ')
if serie_wire.terminada == 's':
    serie_wire.terminada = True
else:
    serie_wire.terminada = False


for element in mis_pelis:
    print(element)
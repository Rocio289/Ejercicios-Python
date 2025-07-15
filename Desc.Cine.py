'''
##En un cine tienen la siguiente política de descuentos.
Si el usuario es minusválido (tiene más de un 33% de minusvalía reconocidad),
se le aplica un descuento a la entrada del 25%.
Si es jubilado(+65 años) también se le aplica el 25 %, y si tiene ambas se le aplica un 35 %.
'''


es_minusvalido = input('¿Tiene minusvalia mayor o igual al 33%? (s/n): ').lower()
if es_minusvalido == 's':
    es_minusvalido = True
else:
    es_minusvalido = False

edad = int(input('¿Qué edad tienes?: '))

def descuento(es_minusvalido, edad):
       
    if es_minusvalido and edad >= 65:
        result = 0.35    
    elif es_minusvalido or edad >= 65:
        result = 0.25    
    else:
        result = 0        
    return result
      
print(f'Tu descuento es de: {descuento(es_minusvalido, edad)*100}%')

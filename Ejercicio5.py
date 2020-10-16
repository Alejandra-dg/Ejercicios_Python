""" Calcular la cantidad de segundos que le toma a luz viajar 
del sol a marte y mostar el resultado en pantalla """

distancia_marte = 227940
velocidad = 299

segundos = distancia_marte/velocidad
minutos = segundos /60

print("la luz tarda", int(segundos), "segundos")
print("la luz tarda", int(minutos), "minutos")
print("en llegar el sol a marte")

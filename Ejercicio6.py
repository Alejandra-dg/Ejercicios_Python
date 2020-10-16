""" Calcular el numero de vueltas que da una llanta en 1km 
dado que el diametro de la llanta es de 50cm mostrar el resultado en pantalla """

diametro = float(50)
constante = float(3.1416)
circunferencia = ((diametro*constante)/100000)

distancia = 1/circunferencia

print("la distancia es: ", distancia)
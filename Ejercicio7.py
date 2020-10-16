""" calcular y mostrar en pantalla la longitud de la sombra de un edificio 
de 20 metros de altura cuando el angulo que forma los rayos de sol con el suelo es 22° """

import math 
 cateto_opuesto= 20
 angulo_elevacion= math.radians(22)

 print("cateto adyacente: es longitud de la sombra")

 tan =  math.tan(angulo_elevacion)
 cateto_adyacente = cateto_opuesto/tan
 print("la longitud de la sombra", cateto_opuesto)
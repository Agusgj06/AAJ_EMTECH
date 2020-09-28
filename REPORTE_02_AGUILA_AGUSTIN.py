#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:41:23 2020

@author: Agustin
"""

import csv

lista_datos = [] 

with open("synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
        lista_datos.append(linea)
   
        
#Opcion 1: Mejor ruta de exportación
"""

direccion = "Exports"
contardor_rutas = 0
rutas_contadas = []
conteo_rutas = []

for ruta in lista_datos:
    
    #Numero de exportaciones = 15408
    #if ruta[1] == direccion:
       # print(ruta)
        #contardor_rutas +=1
        
    if ruta[1] == direccion:
        ruta_actual = [ruta[2], ruta[3]]
        
        if ruta_actual not in rutas_contadas:
            for viaje in lista_datos:
                if ruta_actual == [viaje[2], viaje[3]]:
                    contardor_rutas += 1
                    
        #Total de rutas: 144           
            rutas_contadas.append(ruta_actual)
            conteo_rutas.append([ruta[2], ruta[3], contardor_rutas])
            contardor_rutas = (0)
            
 #Rutas mas populares de mayor a menor           
conteo_rutas.sort(reverse = True, key = lambda x:x[2])

print("Las rutas ordenadas con más número de movimientos son de : ", conteo_rutas)
            



#Opcion 3: Ingresos por ruta
direccion = "Exports"
contardor_rutas = 0
rutas_contadas = []
conteo_rutas = []

for ruta in lista_datos:
    
    #Numero de exportaciones = 15408
    #if ruta[1] == direccion:
       # print(ruta)
        #contardor_rutas +=1
        
    if ruta[1] == direccion:
        ruta_actual = [ruta[2], ruta[3]]
        
        if ruta_actual not in rutas_contadas:
            for viaje in lista_datos:
                if ruta_actual == [viaje[2], viaje[3]]:
                    contardor_rutas += int(viaje[9])
                    
        #Total de rutas: 144           
            rutas_contadas.append(ruta_actual)
            conteo_rutas.append([ruta[2], ruta[3], contardor_rutas])
            contardor_rutas = 0
            
 #Rutas mas populares de mayor a menor           
conteo_rutas.sort(reverse = True, key = lambda x:x[2])
for ingreso_rutas in conteo_rutas:
    print("De: ", ingreso_rutas[0], " a: ", ingreso_rutas[1], " con un monto de: ", int(ingreso_rutas[2]))
    




"""

#ME COSTO MUCHISMO TRABAJO PERO HICE MI MEJOR INTENTO
#GRACIAS :)

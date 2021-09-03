# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

#  construir um programa que simula o resultado do lançamento de um foguete.

distanciaalvo = int(input().strip())
combustivel = int(input().strip())
distanciaatual = 0
possuicombustivel = True

while (distanciaatual < distanciaalvo) and possuicombustivel == True:
    
    distanciaatual = int(distanciaatual + 1)
    
    #calculo do consumo de combustível na iteração atual
    #encontrar a soma dos pares
    menor = 1
    somapares = 0
    
    while int(menor) < distanciaatual:
        if (menor % 2) == 0:
            somapares = int(somapares + menor)
        menor = menor + 1
    somapares = int(somapares + 1)
    
    #calcular consumo de combustivel da etapa
    consumoetapa = float(distanciaalvo / somapares)
    
    if consumoetapa <= combustivel:
        possuicombustivel = True
        combustivel = int(combustivel - consumoetapa)
        print (int(distanciaatual),int(combustivel))
    else: possuicombustivel = False
    
    
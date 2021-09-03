# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

# validar o número de um novo documento da sua empresa.

numero = input ('')

primeiro = int(numero[0])
segundo = int(numero[1])
terceiro = int(numero[2])
quarto = int(numero[3])
quinto = int(numero[4])


if len(numero) == 5:
    verificacao1 = True
else:verificacao1 = False 

if ((segundo ** 4) % 3) == 0:
    verificacao2 = True
else:verificacao2 = False

if ((quarto ** 4) % 3) == 0:
    verificacao3 = True
else:verificacao3 = False

if terceiro not in [0,1]:
    verificacao4 = True
else:verificacao4 = False
 
if (terceiro + quinto) > 3:
    verificacao5 = True
else:verificacao5 = False

if primeiro in [2,5,9]:
    verificacao6 = True
else:verificacao6 = False

print (verificacao1 and verificacao2 and verificacao3 and verificacao4 and verificacao5 and verificacao6)


 




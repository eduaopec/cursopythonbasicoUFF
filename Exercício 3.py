# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

# indicar a menor quantidade de moedas que representa esse valor.

valor = float(input (''))

moeda1 = valor//100
restomoeda1 = valor%100

moeda50 = restomoeda1//50
restomoeda50 = restomoeda1%50

moeda25 = restomoeda50//25
restomoeda25 = restomoeda50%25

moeda10 = restomoeda25//10
restomoeda10 = restomoeda25%10

moeda5 = restomoeda10//5
moeda1S = restomoeda10%5

print (int(moeda1))
print (int(moeda50))
print (int(moeda25))
print (int(moeda10))
print (int(moeda5))
print (int(moeda1S))




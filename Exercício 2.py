# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

# indicar a menor quantidade de moedas que representa esse valor.

valor = float(input (''))

moedade1 = valor//100
restomoeda1 = valor%100

moedade50 = restomoeda1//50
restomoeda50 = restomoeda1%50

moeda25 = restomoeda50//25
restomoeda25 = restomoeda50%25

moeda10 = restomoeda25//10
moeda1S = restomoeda25%10

print (moeda1)
print (moeda50)
print (moeda25)
print (moeda10)
print (moeda1S)




# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

# simular um personagem andando em uma sala escura.

posicao = 'I'
resultado = ''

while resultado not in ['X', 'V', 'P3', 'P2', 'P1', 'E']:
    
    entrada = input().strip()
    
    if entrada in ['D','E','C','B']:
        
        if posicao == 'I':
            if entrada == 'D':
                posicao = 'O1'
            elif entrada == 'B':
                resultado = 'X'
                print ('X')
        elif posicao == 'O1': 
            if entrada == 'D':
                posicao = 'O2'
            elif entrada == 'B':
                resultado = 'P3'
                print ('P3')
            elif entrada == 'E':
                resultado = 'V'
                print ('V')
        elif posicao == 'O2': 
            if entrada == 'B':
                posicao = 'O3'
            elif entrada == 'D':
                resultado = 'X'
                print ('X')
            elif entrada == 'E':
                resultado = 'V'
                print ('V')
        elif posicao == 'O3': 
            if entrada == 'B':
                resultado = 'P2'
                print ('P2')
            elif entrada == 'D':
                resultado = 'P1'
                print ('P1')
            elif entrada == 'E':
                resultado = 'P3'
                print ('P3')
    else:
        resultado = 'E'
        print ('E')
        
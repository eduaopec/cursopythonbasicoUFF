# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

#  preenchendo matrix de 2 dimensões

# criando a matriz das notas da turma
notas = []
 
for i in range(3):
     # cria linha em branco
     linha = []
     
     # preenche a linha criada de nota
     for j in range(5):
         msg = f'Nota {j+1} do aluno {i+1}? '
         linha.append (float(input(msg)))

     # adiciona a linha na matriz de turma
     notas.append(linha)
     
     
for i in range (3):
    print (notas[i])

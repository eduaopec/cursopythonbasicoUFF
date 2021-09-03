# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

# Faça um programa para gerenciar sua coleção de vinhos. 
# O programa deve permitir que o usuário insira dados sobre vinhos e realize 
# consultas sobre as garrafas já cadastradas.

nome = []
tipo = []
quantidade = []
comando = 0
i = 0
totalquantidade = 0
parametronome = ''
parametrotipo= ''
totaltipo = 0

while comando != -1:
        comando = int(input ())
        if comando in [1,2,3,4,-1]:

            if comando == 1:
                nome.append (input())
                tipo.append (input())
                quantidade.append (input())

            if comando == 2:
                parametronome = input()
                if len(nome) > 0:
                    for i in range (len(nome)):
                            if nome[i] == parametronome:
                                print (tipo[i])
                                print (quantidade[i])
                    if parametronome not in nome:
                       print ("Não cadastrado")
                else:
                    print ("Não cadastrado")
                    
            if comando == 3:    
                totaltipo = 0
                parametrotipo = input()
                if len(tipo) > 0:
                    for i in range (len(tipo)):
                            if tipo[i] == parametrotipo:
                                totaltipo = totaltipo + int(quantidade[i])
                    if parametrotipo in tipo:
                       print (totaltipo)
                    else:
                       print ("Não cadastrado")
                else:
                    print ("Não cadastrado")
                    
            if comando == 4:
                totalquantidade = 0
                for i in range (len(quantidade)):
                    totalquantidade = totalquantidade + int(quantidade[i])
                print (totalquantidade)    
        else:
            print ("Inválido")



# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

# simular a análise de uma eleição

nomes = input().strip() # string com o nome dos candidatos separados por vírgula
candidatos = [] #lista de candidatos
votos = [] # lista dos votos por seção eleitoral
linha = [] # linha de votos
totalvotossecao = 0 # total de votos de uma seção
totalvotoscandidato = 0 # total de votos de um candidato
totalvotosrecebidocandidato = [] #matriz de candidatos e total de seus votos
totalvotos = 0 #total de votos
matrizordenada = []

inicio = 0
fim = 0
i = 0
j = 0

comando = 0
entrada = ''

if len(nomes) != 0: 
    # econtrando os nomes no texto e gerando a lista de candidatos
    inicio = 0
    fim = nomes.find (',', inicio)

    # gerando lista de candidato
    while fim != -1:
        candidatos.append([nomes[inicio:fim]])
        inicio = fim + 1
        fim = nomes.find (',', inicio)
 
    candidatos.append([nomes[inicio:len(nomes)]])

while comando != 6:
        comando = int(input ())
        if comando in [1,2,3,4,5]:
            if comando == 1: # o usuário informa os votos dos candidatos em uma seção eleitoral.
                # inserindo uma nova seção eleitoral com zero votos
                linha = []
                for i in range(len(candidatos)):
                    linha.append(0)               
                votos.append(linha)     

                entrada = input().strip() + ","
                inicio = 0
                fim = entrada.find (',', inicio)
                i = 0
                for i in range(len(candidatos)):
                    votos[len(votos)-1][i] = int(entrada[inicio:fim])
                    totalvotos = totalvotos + votos[len(votos)-1][i]
                    inicio = fim + 1
                    fim = entrada.find (',', inicio)
 
                j = 0
                for j in range(len(votos)):
                    totalvotossecao = 0
                    for i in range(len(candidatos)):
                        totalvotossecao = totalvotossecao + int(votos[j][i])         
 
                if len(totalvotosrecebidocandidato)>0:
                    totalvotosrecebidocandidato.clear()
                j = 0
                for j in range(len(candidatos)):
                    totalvotoscandidato = 0
                    for i in range(len(votos)):
                        totalvotoscandidato = totalvotoscandidato + int(votos[i][j])         
                    totalvotosrecebidocandidato.append([candidatos[j],totalvotoscandidato]) 
   
                # apagando os elementos da lista de ordenação se eles existirem 
                if len(matrizordenada)>0:    
                    matrizordenada.clear()
                #criando a matriz ordenada por total de votos dos candidatos por ordem decrescente
                matrizordenada = sorted(totalvotosrecebidocandidato, key= lambda media: media[1], reverse=True) 
 
            if comando == 2: # números inteiros, um por linha, indicando o total de votos de cada seção, na mesma ordem que as seções foram registradas via opção 1.
               j = 0
               for j in range(len(votos)):
                   totalvotossecao = 0
                   for i in range(len(candidatos)):
                       totalvotossecao = totalvotossecao + int(votos[j][i])         
                   print(str(totalvotossecao))                   
                    
            if comando == 3: # números inteiros, um por linha, indicando o total de votos de cada candidato, na mesma ordem usada para informar os nomes dos candidatos.
                j = 0
                for j in range(len(candidatos)):
                    totalvotoscandidato = 0
                    for i in range(len(votos)):
                        totalvotoscandidato = totalvotoscandidato + int(votos[i][j])         
                    print(str(totalvotoscandidato))

            if comando == 4: # nomes dos candidatos, um por linha, em ordem decrescente do número de votos recebidos pelos candidatos.
                for i in range(len(matrizordenada)):
                    nomes = str(matrizordenada[i][0])
                    # retirando os caracteres , ; e . do parágrafo
                    caracteres = "]['"
                    for j in range(0,len(caracteres)):
                        nomes = nomes.replace (caracteres[j], "")
                    print (nomes)    
            
            if comando == 5: # "Terá segundo turno." caso o candidato em 1o. lugar não some mais de 50% dos votos. "Não terá segundo turno." caso contrário.
                if len(votos) > 0:
                    if matrizordenada[0][1] < int(totalvotos/2): 
                        print ('Terá segundo turno.')
                    else:
                        print ('Não terá segundo turno.')
                    
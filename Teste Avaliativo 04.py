# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

# O seu programa deve primeiramente retirar os caracteres de pontuação 
# (ponto, vírgula e ponto e vírgula) do texto. Feito isso, deverá processá-lo 
# e exibir algumas estatísticas sobre o texto processado.

paragrafo = input().strip()
palavras = input()
if len(paragrafo) != 0 or len(palavras.strip()) != 0: 
    lista_palavras = []
    lista_palavras_upper = []
    lista_palavras_selecao = []
    lista_palavras_selecao_upper = []
    lista_palavras_selecao_contagem = []

    # retirando os caracteres , ; e . do parágrafo
    caracteres = ".,;"
    for i in range(0,len(caracteres)):
        paragrafo = paragrafo.replace (caracteres[i], "")

    # econtrando as palavras no texto e gerando a lista de palavras
    inicio = 0
    fim = paragrafo.find (' ', inicio)

    # gerando lista de palavras e as mesmas em maisculas do paragrafo de entrada
    while fim != -1:
        lista_palavras.append(paragrafo[inicio:fim])
        lista_palavras_upper.append(paragrafo[inicio:fim].upper())
        inicio = fim + 1
        fim = paragrafo.find (' ', inicio)
 
    lista_palavras.append(paragrafo[inicio:len(paragrafo)])
    lista_palavras_upper.append (paragrafo[inicio:len(paragrafo)].upper())

    palavras = palavras + " "  
    inicio = 0
    fim = palavras.find (' ', inicio)

    # gerando lista de palavras selecao e as mesmas em maisculas da lista de seleção sem repetição
    palavraincluida = ""
    while fim != -1:
        if (palavras[inicio:fim].upper()) not in lista_palavras_selecao_upper:
            lista_palavras_selecao.append(palavras[inicio:fim])
            lista_palavras_selecao_upper.append(palavras[inicio:fim].upper())
            palavraincluida = palavras[inicio:fim]
            inicio = fim + 1
            fim = palavras.find (' ', inicio)
        else:    
            inicio = fim + 1
            fim = palavras.find (' ', inicio)

    #if (palavraincluida not in lista_palavras_selecao) and palavraincluida != "":
    #    lista_palavras_selecao.append(palavras[inicio:len(palavras)])
    #    lista_palavras_selecao_upper.append (palavras[inicio:len(palavras)].upper())

    # usar o método find para encontrar as palavras no parágrafo e fazer a contagem
    # calcular o maior percentual

    indicedomaior = 0
    maiorpercentual = 0
    j = 0
    for j in range (len(lista_palavras_selecao_upper)):
        palavraupper = lista_palavras_selecao_upper[j]
        if palavraupper != "":
            contagem = 0
            contagem = lista_palavras_upper.count(palavraupper)
            lista_palavras_selecao_contagem.append(contagem)
            if round(((contagem/len(lista_palavras))*100),3) > maiorpercentual:
                indicedomaior = j
                maiorpercentual = round((contagem/(len(lista_palavras)))*100,3)

    i = 0
    if maiorpercentual > 0:
        print (len(lista_palavras))
        for i in range (len(lista_palavras_selecao)):
            print (lista_palavras_selecao[i],lista_palavras_selecao_contagem[i])
        print (lista_palavras_selecao[indicedomaior], str("{0:.3f}".format(maiorpercentual) + '%'))
    elif len(paragrafo)!= 0:
        print (len(lista_palavras))
#else:
#    print ("não tenho o que fazer")
        
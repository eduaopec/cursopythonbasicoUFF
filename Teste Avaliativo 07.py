# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

# permitir análises de autonomia de diferentes automóveis sob diferentes condições de transito (urbano e rodoviário). 

autonomiatotal = 0 #somatório de todas as autonomias que foram inputadas
quantidadetotal = 0 #somatório da quantidade de medidas imputados
modeloautdecrescurbrod = [] # modelos dos automóveis, um por linha, ordenados decrescentemente pela autonomia média, considerando tanto trânsito urbano quanto rodoviário.
modeloautcrescurb = [] # modelos dos automóveis, um por linha, ordenados crescentemente pela autonomia média, considerando somente trânsito urbano.
quantidadeopcao5 = 0 # um número inteiro que representa a quantidade de automóveis que têm ao menos uma medida de autonomia em trânsito urbano maior que alguma medida de autonomia em trânsito rodoviário.

modelo = ''
autonomiaurb1 = 0
autonomiaurb2 = 0
autonomiaurb3 = 0
autonomiarod1 = 0
autonomiarod2 = 0
autonomiarod3 = 0

inicio = 0
fim = 0
i = 0

comando = 0
entrada = ''

while comando != 6:
        comando = int(input ())
        if comando in [1,2,3,4,5]:
            if comando == 1: # o usuário informa os seguintes dados separados por ponto e vírgula: o modelo do automóvel (string), três medidas da sua autonomia em trânsito urbano e três medidas da sua autonomia em transito rodoviário.
               entrada = input().strip() + "*"
               
               # lendo os parâmetros da entrada separados por ponto e vírgula
               inicio = 0
               fim = entrada.find (';', inicio)
               modelo = entrada[inicio:fim]
               inicio = fim + 1
               fim = entrada.find (';', inicio)
               autonomiaurb1 = round(float(entrada[inicio:fim]),1)
               inicio = fim + 1
               fim = entrada.find (';', inicio)
               autonomiaurb2 = round(float(entrada[inicio:fim]),1)
               inicio = fim + 1
               fim = entrada.find (';', inicio)
               autonomiaurb3 = round(float(entrada[inicio:fim]),1)
               inicio = fim + 1
               fim = entrada.find (';', inicio)
               autonomiarod1 = round(float(entrada[inicio:fim]),1)
               inicio = fim + 1
               fim = entrada.find (';', inicio)
               autonomiarod2 = round(float(entrada[inicio:fim]),1)
               inicio = fim + 1
               fim = entrada.find ('*', inicio)
               autonomiarod3 = round(float(entrada[inicio:fim]),1)
               
               #print (autonomiaurb1)
               #print (autonomiaurb2)
               #print (autonomiaurb3)
               #print (autonomiarod1)
               #print (autonomiarod2)
               #print (autonomiarod3)
                              
               #somatória de todas autonomias de um modelo
               autonomiatotalmodelo = 0
               autonomiatotalmodelo = round(autonomiaurb1 + autonomiaurb2 + autonomiaurb3 + autonomiarod1 + autonomiarod2 + autonomiarod3,1)

               #print (autonomiatotalmodelo) 

               #somatória das autonomias urbanas de um modelo
               autonomiatotalurbanamodelo = 0
               autonomiatotalurbanamodelo = round(autonomiaurb1 + autonomiaurb2 + autonomiaurb3,1)

               #print (autonomiatotalurbanamodelo) 

               #somatório de todas as autonomias que foram inputadas
               autonomiatotal = autonomiatotal + autonomiaurb1 + autonomiaurb2 + autonomiaurb3 + autonomiarod1 + autonomiarod2 + autonomiarod3 

               #somatório da quantidade de medidas imputados
               quantidadetotal = quantidadetotal + 6

               #matriz de médias de autonomia total por modelo
               modeloautdecrescurbrod.append([modelo,round(autonomiatotalmodelo/6,1)]) 

               #print (modeloautdecrescurbrod)         

               #matriz de médias de autonomia urbana por modelo
               modeloautcrescurb.append([modelo,round(autonomiatotalurbanamodelo/3,1)])               

               #print (modeloautcrescurb)         

               if (autonomiaurb1 > autonomiarod1) or (autonomiaurb1 > autonomiarod2) or (autonomiaurb1 > autonomiarod3) or (autonomiaurb2 > autonomiarod1) or (autonomiaurb2 > autonomiarod2) or (autonomiaurb2 > autonomiarod3) or (autonomiaurb3 > autonomiarod1) or (autonomiaurb3 > autonomiarod2) or (autonomiaurb3 > autonomiarod3):
                   quantidadeopcao5 = int(quantidadeopcao5 + 1) 

            if comando == 2: # um número real que representa a autonomia média considerando todas as medições de todos os automóveis cadastrados em todas as condições de trânsito.
               if quantidadetotal != 0:
                  print(str(round(autonomiatotal/quantidadetotal,1)))                   
               else:
                  print ('0.0') 
                    
            if comando == 3: # modelos dos automóveis, um por linha, ordenados decrescentemente pela autonomia média, considerando tanto trânsito urbano quanto rodoviário.
                #criando a matriz ordenada por média de autonomia total em ordem decescente    
                matrizordenada = sorted(modeloautdecrescurbrod, key= lambda media: media[1], reverse=True) 
                for i in range(len(matrizordenada)):
                    print (matrizordenada[i][0])    

            if comando == 4: # modelos dos automóveis, um por linha, ordenados crescentemente pela autonomia média, considerando somente trânsito urbano.
                #criando a matriz ordenada por média de autonomia urbana em ordem crescente
                matrizordenada = sorted(modeloautcrescurb, key= lambda media: media[1]) 
                for i in range(len(matrizordenada)):
                    print (matrizordenada[i][0])    
            
            if comando == 5: # um número inteiro que representa a quantidade de automóveis que têm ao menos uma medida de autonomia em trânsito urbano maior que alguma medida de autonomia em trânsito rodoviário.
                print (quantidadeopcao5)

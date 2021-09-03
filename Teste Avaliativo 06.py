# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:24:31 2021

@author: Windows 7
"""

#  simular um experimento para análise da eficácia de uma vacina de COVID-19. 


totalm = 0 #masculino ok
totalf = 0 #feminino ok

totalj = 0 #jovem ok
totala = 0 #adulto ok
totali = 0 #idoso ok

totalv = 0 #vacinado ok
totalp = 0 #placebo ok

totalc = 0 #com COVID ok
totalnc = 0 #sem COVID ok

totalpi = 0 #placedo infectado ok
totalvi = 0 #vacina infectado ok

totalpim = 0 #placebo infectado masculino ok
totalpif = 0 #placebo infectado feminimo ok
totalvif = 0 #vacinado infectado feminino ok
totalvim = 0 #vacinado infectado masculino ok

totalpij = 0 #placebo infectado jovem ok
totalpia = 0 #placebo infectado adulto ok
totalpii = 0 #placebo infectado idoso ok
totalvij = 0 #vacinado infectado jovem ok
totalvia = 0 #vacinado infectado adulto ok
totalvii = 0 #vacinado infectado idoso ok


participantes = 0
i = 0
entrada = ''

genero = ''
idade = 0
grupo = ''
contraiu = ''

faixa = 0

comando = 0

participantes = int (input())

for i in range (participantes):

    entrada = input().strip()

    # lendo os parâmetros da entrada separados por vírgula
    inicio = 0
    fim = entrada.find (',', inicio)
    genero = entrada[inicio:fim]
    inicio = fim + 1
    fim = entrada.find (',', inicio)
    idade = int(entrada[inicio:fim])
    inicio = fim + 1
    fim = entrada.find (',', inicio)
    grupo = entrada[inicio:fim]
    inicio = fim + 1
    fim = inicio + 1
    contraiu = entrada[inicio:fim]
    
    # totais por genero
    if genero == 'F':
        totalf = totalf + 1 #total feminino
        if contraiu == 'S' and grupo == 'P': #feminino com COVID e placebo
            totalpif = totalpif + 1
        elif contraiu == 'S' and grupo == 'V': #feminino com COVID e vacinado
            totalvif = totalvif + 1
    else: #masculino
        totalm = totalm + 1 #total masculino
        if contraiu == 'S' and grupo == 'P': #masculino com COVID e placebo
            totalpim = totalpim + 1
        elif contraiu == 'S' and grupo == 'V': #masculino com COVID e vacinado
            totalvim = totalvim + 1
    
    # definindo a faixa etária
    if idade >= 0 and idade <= 19:
        faixa = 1
    elif idade > 19 and idade <= 60:
        faixa = 2
    else:
        faixa = 3
        
    #totais por faixa etária    
    if faixa == 1: #de 0 a 19 anos
        totalj = totalj + 1 #total 0 a 19 anos
        if contraiu == 'S' and grupo == 'P': #jovem com COVID e placebo
            totalpij = totalpij + 1
        elif contraiu == 'S' and grupo == 'V': #jovem com COVID e vacinado
            totalvij = totalvij + 1
    elif faixa == 2: #de 20 a 59 anos
        totala = totala + 1 #total 20 a 59 anos
        if contraiu == 'S' and grupo == 'P': #adulto com COVID e placebo
            totalpia = totalpia + 1
        elif contraiu == 'S' and grupo == 'V': #adulto com COVID e vacinado
            totalvia = totalvia + 1
    else: #acima de 60 anos
        totali = totali + 1 #total acima de 60 anos
        if contraiu == 'S' and grupo == 'P': #idoso com COVID e placebo
            totalpii = totalpii + 1
        elif contraiu == 'S' and grupo == 'V': #jovem com COVID e vacinado
            totalvii = totalvii + 1

    #totais por infectado ou não    
    if contraiu == 'S':
        totalc = totalc + 1 #total com COVID
        if contraiu == 'S' and grupo == 'P': #com COVID e placebo
            totalpi = totalpi + 1
        elif contraiu == 'S' and grupo == 'V': #com COVID e vacinado
            totalvi = totalvi + 1
    else: #sem COVID
        totalnc = totalnc + 1 #total sem COVID

    #totais por vacinado ou placebo
    if grupo == 'P':
        totalp = totalp + 1 #total com placebo
    else: 
        totalv = totalv + 1 #total com vacina
            
#print('masculino:',totalm) #masculino 
#print('feminino:',totalf) #feminino 

#print('jovem:',totalj) #jovem
#print('adulto:',totala) #adulto 
#print('idoso:',totali) #idoso 

#print('vacinado:',totalv) #vacinado 
#print('placebo:',totalp) #placebo 

#print('com COVID:',totalc) #com COVID 
#print('sem COVID:',totalnc) #sem COVID 

#print('placebo infectado:',totalpi) #placedo infectado 
#print('vacina infectado:',totalvi) #vacina infectado 

#print('placebo infectado masculino:',totalpim) #placebo infectado masculino 
#print('placebo infectado feminino:',totalpif) #placebo infectado feminimo 
#print('vacinado infectado masculino:',totalvim) #vacinado infectado masculino 
#print('vacinado infectado feminino:',totalvif) #vacinado infectado feminimo 

#print('placebo infectado jovem:',totalpij) #placebo infectado jovem 
#print('placebo infectado adulto:',totalpia) #placebo infectado adulto 
#print('placebo infectado idoso:',totalpii) #placebo infectado idoso 
#print('vacinado infectado jovem:',totalvij) #vacinado infectado jovem 
#print('vacinado infectado adulto:',totalvia) #vacinado infectado adulto 
#print('vacinado infectado idoso:',totalvii) #vacinado infectado idoso 

while comando != 5:
        comando = int(input ())
        if comando in [1,2,3,4]:
            if comando == 1: # na primeira linha, os percentuais de participantes do gênero masculino e feminino, separados por vírgula. Na segunda linha os percentuais de jovens, adultos e idosos, separados por vírgula. Na terceira linha, os percentuais de participantes que receberam vacina e placebo, separados por vírgula. Na quarta linha, os percentuais de participantes que contrairam e não contraíram COVID, separados por vírgula.
                # masculino x feminimo
                print(str(int(100*(totalm/participantes)))+'%,',str(int(100*(totalf/participantes)))+'%',sep='')                
                # jovem x adulto x idoso
                print(str(int(100*(totalj/participantes)))+'%,',str(int(100*(totala/participantes)))+'%,',str(int(100*(totali/participantes)))+'%',sep='')
                # vacina x placebo
                print(str(int(100*(totalv/participantes)))+'%,',str(int(100*(totalp/participantes)))+'%',sep='')
                # infectado x não infectado
                print(str(int(100*(totalc/participantes)))+'%,',str(int(100*(totalnc/participantes)))+'%',sep='')

            if comando == 2: # eficácia geral da vacina
                print(str(int(100*(totalpi-totalvi)/totalpi))+'%')                   
                
            if comando == 3: # um percentual de eficácia por linha, onde a primeira linha restringe a população somente aos participantes do gênero masculino e a segunda linha restringe a população somente aos participantes do gênero feminino.    
                # eficácia geral masculina
                if totalpim != 0:
                    print(str(int(100*(totalpim-totalvim)/totalpim))+'%')
                else: 
                    print ('0%')
                # eficácia geral feminina
                if totalpif != 0:
                    print(str(int(100*(totalpif-totalvif)/totalpif))+'%')
                else:        
                    print ('0%')
                    
            if comando == 4: # um percentual de eficácia por linha, onde a primeira linha restringe a população somente aos participantes jovens, a segunda linha restringe a população somente aos participantes adultos e a terceira linha restringe a população somente aos participantes idosos.
                # eficácia geral jovem
                if totalpij != 0:
                    print(str(int(100*(totalpij-totalvij)/totalpij))+'%')
                else:        
                    print ('0%')
               # eficácia geral adulto
                if totalpia != 0:
                    print(str(int(100*(totalpia-totalvia)/totalpia))+'%')
                else:        
                    print ('0%')
               # eficácia geral idoso
                if totalpii != 0:
                    print(str(int(100*(totalpii-totalvii)/totalpii))+'%')
                else:        
                    print ('0%')
          



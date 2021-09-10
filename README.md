# cursopythonbasicoUFF
Enunciados dos exercícios do curso.
Os testes dos exercícios e dos testes avaliativos foram executados no run.codes (https://run.codes)

#########################################
Exercício 1
Faça um programa que exiba o perímetro de uma circunferência a partir do seu raio (float).

Para simplificar, usem pi = 3.1416

P = 2 * pi * r

Exemplo:

Entrada: 10

Saída: 62.832

#########################################
Exercício 2
Faça um programa que informe a distância em quilômetros (float) de um raio para o observador.

O observador deve informar o tempo (float, em segundos) transcorrido entre ver o raio e ouvir o trovão.
Assuma que a velocidade do som é 340 m/s.

Exemplo:
Entrada: 3

Saída: 1.02

#########################################
Exercício 3
Faça um programa para, a partir de um valor informado em centavos, indicar a menor quantidade de moedas que representa esse valor.

Considere moedas de 1, 5, 10, 25 e 50 centavos, e 1 real.
A saída deve ser a quantidade de cada moeda, uma por linha, em ordem decrescente de valor.
Dicas:
Para fazer uma divisão inteira em Python, use o operador //.
Para descobrir o resto de uma divisão, use o operador %.
Exemplo:
Para uma entrada de 290 centavos, a menor quantidade de moedas é 2 moedas de 1 real, 1 moeda de 50 centavos, 1 moeda de 25 centavos, 1 moeda de 10 centavos, 1 moeda de 5 centavos e 0 moedas de 1 centavo.

Entrada: 290

Saída:

2

1

1

1

1

0

#########################################
Teste Avaliativo 01

Descrição
Você ficou encarregado de criar um programa para validar o número de um novo documento da sua empresa. Como é um documento sensível, algumas regras foram criadas para que seja mais difícil alguém criar um número falso.

Regras
Regra 1: O número do documento deve ter 5 dígitos no total. Exemplo: 23265. Neste exemplo, o primeiro dígito é o 2, o segundo é o 3, o terceiro é o 2 e assim por diante.
Regra 2: O segundo dígito elevado a 4 deve ser divisível por 3. A mesma regra deve valer para o quarto dígito.
Regra 3: O terceiro dígito não pode ser 0 nem 1.
Regra 4: A soma do terceiro com o último dígito deve ser maior que 3.
Regra 5: O primeiro dígito deve necessariamente ser 2, 5 ou 9.
Seu programa deverá receber como entrada um número de documento e deverá exibir True caso o número seja válido de acordo com as regras acima, ou False caso contrário.

Exemplos:
Input	Output
23265	True
12345	False

#########################################
Teste Avaliativo 02

Descrição
Construa um programa para simular um personagem andando em uma sala escura. O programa recebe como entrada comandos direcionais para o personagem andar. Somente os comandos na tabela abaixo são aceitos pelo programa. Se um comando inválido for dado como entrada, ele deve exibir a mensagem “E” e terminar.

Entrada	Ação
D	Personagem anda para a direita.
E	Personagem anda para a esquerda.
C	Personagem anda para cima.
B	Personagem anda para baixo.
O programa deve se basear no seguinte mapa visto de cima:

INÍCIO	O	O	X
X	PORTA 3	O	PORTA 1
X	X	PORTA 2	X
No mapa acima, o personagem começa no piso “INÍCIO”. Os pisos marcados com “O” são pisos onde o personagem pode passar. Os pisos marcados com “X” são pisos onde o personagem não pode passar. Se o personagem chegar em um piso com “X”, deverá ser exibida a mensagem correspondente da tabela abaixo e o programa deverá terminar. Leve em consideração as ações da tabela e os resultados de cada ação ao fazer o seu programa. O programa deve esperar uma entrada caso o piso onde se encontra o personagem seja o INÍCIO ou um piso marcado com “O”.

Lembrem-se que as mensagens de saída do programa devem estar exatamente iguais à tabela e exemplos abaixo. Se você usar x ao invés de X, seu programa não estará correto.

Ação	Resultado
Andar para um piso marcado com “X”.	Exibir a mensagem “X” e terminar o programa.
Andar de volta para o piso onde acabou de passar.	Exibir a mensagem “V” e terminar o programa.
Chegar no piso PORTA 3.	Exibir a mensagem “P3” e terminar o programa.
Chegar no piso PORTA 2.	Exibir a mensagem “P2” e terminar o programa.
Chegar no piso PORTA 1.	Exibir a mensagem “P1” e terminar o programa.
Inserir um comando desconhecido.	Exibir a mensagem "E" e terminar o programa.
Exemplos:
Entrada	Saída
A	E
D
B	P3
D
D
D	X

#########################################
Teste Avaliativo 03

Descrição
Você foi contratado pela empresa SpaceX para construir um programa que simula o resultado do lançamento de um foguete.

O programa deve receber como entrada:
A distância esperada (inteiro) que o foguete deve chegar em km (distância alvo), em relação ao solo.
A quantidade de combustível (inteiro) disponível inicialmente, em kg.
O programa deve exibir como saída:
A cada km percorrido com sucesso, deve exibir o total de kms percorridos até o momento e a quantidade atual de combustível disponível. Essas informações são separadas por um espaço. Os valores deverão ser exibidos como inteiros (sem casa decimal). Use a função (int) para transformá-los. Exemplo: se em um dado momento o foguete percorreu 50km e ainda tem 30kg de combustível, deve imprimir: 50 30.
Você deve considerar no programa que o foguete irá percorrer 1 km por vez (iteração). O programa deve terminar no momento que o foguete chegar até a distância esperada ou quando a quantidade de combustível disponível não for suficiente para percorrer o próximo kilômetro.

A cada iteração do programa, você deve calcular quanto de combustível ainda resta subtraindo o consumo de combustível da quantidade de combustível atual. Use as regras abaixo para calcular o consumo de combustível a cada iteração.

Consumo de combustível
O consumo de combustível depende da distância atual do foguete em relação ao solo e da distância alvo.

Para calcular o consumo, usaremos duas etapas:

A primeira etapa, que iremos chamar de soma_pares, é a soma dos números inteiros pares menores que a distância atual, mais um.
A segunda etapa é a divisão da distância alvo por soma_pares.
Por exemplo, considere que a distância atual é 10km e a distância alvo é 20km.

Primeira etapa: A soma dos números pares inteiros menores que 10 é 20, mais um, 21.
Segunda etapa: 20 / 21 = 0.952. Ou seja, o consumo nessa iteração é de 0.952kg de combustível.
Como outro exemplo, considere que a distância atual é 1km e a distância alvo é 4km.

Primeira etapa: A soma dos números pares inteiros menores que 1 é 0, mais um, 1.
Segunda etapa: 4 / 1 = 4. Ou seja, o consumo nessa iteração é de 4kg de combustível.
Exemplos de entrada e saída:
Entrada	Saída
10
25	1 15
2 5
3 1
5
25	1 20
2 15
3 13
4 11
5 10
Passo a passo do exemplo 1:
Considere que foram dados como entrada ao programa os valores 10 e 25. Ou seja, o usuário quer saber se o foguete consegue chegar a 10km de distância com 25kg de combustível.

Na primeira iteração (1km de distância) o consumo de combustível será 10/1 = 10kg. Após percorrer 1km, o foguete tem agora 15kg de combustível restantes. O programa imprime 1 15 na tela.

Na segunda iteração (2km de distância), o consumo de combustível será 10/1 = 10kg. Após percorrer 2km, o foguete tem agora 5kg de combustível restantes. O programa imprime 2 5 na tela.

Na terceira iteração (3km de distância), o consumo de combustível será 10/3 = 3.33kg. Após percorrer 3km, o foguete tem agora 1.67kg de combustível restantes. O programa imprime 3 1 na tela.

Na quarta iteração (4km de distância), o consumo de combustível será 10/3 = 3.33kg. Entretanto, o foguete tem apenas 1.67kg de combustível restantes. Logo, como ele não tem a quantidade suficiente para continuar, o programa termina.

Passo a passo do exemplo 2:
Considere que foram dados como entrada ao programa os valores 5 e 25.

Na primeira iteração (1km de distância) o consumo de combustível será 5/1 = 5kg. Após percorrer 1km, o foguete tem agora 20kg de combustível restantes. O programa imprime 1 20 na tela.

Na segunda iteração (2km de distância), o consumo de combustível será 5/1 = 5kg. Após percorrer 2km, o foguete tem agora 15kg de combustível restantes. O programa imprime 2 15 na tela.

Na terceira iteração (3km de distância), o consumo de combustível será 5/3 = 1.66kg. Após percorrer 3km, o foguete tem agora 13.34kg de combustível restantes. O programa imprime 3 13 na tela.

Na quarta iteração (4km de distância), o consumo de combustível será 5/3 = 1.66kg. Após percorrer 4km, o foguete tem agora 11.68kg de combustível restantes. O programa imprime 4 11 na tela.

Na quinta iteração (5km de distância), o consumo de combustível será 5/7 = 0.71kg. Após percorrer 5km, o foguete tem agora 10.97kg de combustível restantes. O programa imprime 5 10 na tela.

Como o foguete atingiu a distância alvo (5km), o programa termina.

#########################################
Teste Avaliativo 04

Descrição
Desenvolva um programa que receba duas entradas. A primeira é um parágrafo de um texto. A segunda é uma lista de palavras.

Entradas:
um texto (sem quebra de linhas).
uma lista de palavras separadas por espaço.
O seu programa deve primeiramente retirar os caracteres de pontuação (ponto, vírgula e ponto e vírgula) do texto. Feito isso, deverá processá-lo e exibir algumas estatísticas sobre o texto processado, conforme lista de saídas abaixo:

Saídas:
Quantidade de palavras no texto.
Considere que qualquer conjunto de caracteres separados por espaço é uma palavra. A única exceção é quando o texto possui uma única palavra. Nesse caso não existe espaço.
Para cada palavra da lista de palavras, exibir a palavra e a quantidade de vezes que ela aparece no texto.
Por exemplo, se a palavra 'goiaba' aparece duas vezes no texto, e ela está na lista de palavras, então o programa deve imprimir: goiaba 2
Se a lista for vazia, não imprimir essa informação.
Imprimir a palavra da lista que mais aparece no texto e a proporção em que ela aparece, em relação à quantidade total de palavras no texto.
Usar arredondamento com 3 casas decimais.
Por exemplo, se 'goiaba' foi a palavra da lista que mais apareceu no texto, tendo aparecido duas vezes e o texto tendo 10 palavras no total: goiaba 20.000%
Se nenhuma palavra da lista apareceu no texto, não imprimir essa informação.
Se houver empate, escolha a que aparece primeiro na lista de palavras.
Observação: desconsidere diferenças entre letras maiúsculas e minúsculas durante o processamento. Por exemplo, seu programa deve considerar que Graduação e graduação é a mesma palavra. No entanto, note que na saída do programa, minusculas e maiúsculas fazem diferença!

Exemplo
Entrada
A Universidade Federal Fluminense (UFF) é uma universidade pública de ensino superior com sede em Niterói, no Estado do Rio de Janeiro.

universidade rio

Saída
22

universidade 2

rio 1

universidade 9.091%

#########################################
Teste Avaliativo 05

Descrição
Faça um programa para gerenciar sua coleção de vinhos. O programa deve permitir que o usuário insira dados sobre vinhos e realize consultas sobre as garrafas já cadastradas.

O programa irá funcionar baseado em um menu de opções. Ele deve continuar aguardando novas opções enquanto a opção escolhida for diferente de -1.
A opção 1 irá permitir que uma nova garrafa de vinho seja cadastrada.
Cada vinho inserido deve ter as seguintes informações: nome, tipo e quantidade. Cada um em uma linha.
Exemplo:
Usuário escolhe a opção 1.
Usuário insere o nome do vinho: Colina
Usuário insere o tipo do vinho: tinto suave
Usuário insere a quantidade: 10
A opção 2 irá permitir a consulta por nome dos vinhos já cadastrados. Caso o vinho seja encontrado, deverá ser exibido o seu tipo e a quantidade disponível. Um por linha.
Assuma que somente um vinho com o mesmo nome será cadastrado. Não é necessário fazer essa verificação.
Exemplo:
Usuário escolhe a opção 2.
Usuário insere o nome a ser buscado: Colina
Programa imprime: tinto suave
Programa imprime: 10
Se o vinho não for encontrado, deverá ser exibida a mensagem "Não cadastrado".
A opção 3 irá permitir a consulta por tipo dos vinhos já cadastrados. Caso o tipo seja encontrado, deverá ser exibida a soma da quantidade de garrafas cadastradas com o tipo escolhido.
Exemplo (assumindo que existem 15 garrafas de outro vinho tinto suave além do Colina que foram cadastradas anteriormente):
Usuário escolhe a opção 3.
Usuário insere o tipo a ser buscado: tinto suave
Programa imprime: 25
Se o tipo não for encontrado, deverá ser exibida a mensagem "Não cadastrado".
A opção 4 imprime a soma total da quantidade de vinhos cadastrados até o momento. Observe que é a soma das quantidades e não a contagem de vinhos cadastrados.
Exemplo:
Usuário escolhe a opção 4.
Programa imprime: 10.
Se uma opção inválida for escolhida, deve exibir a mensagem "Inválido".
Exemplo
Usuário escolhe a opção 1.
Usuário insere o nome do vinho: Colina
Usuário insere o tipo do vinho: tinto
Usuário insere a quantidade: 10
Usuário escolhe a opção 1.
Usuário insere o nome do vinho: Seleção
Usuário insere o tipo do vinho: tinto
Usuário insere a quantidade: 13
Usuário escolhe a opção 1.
Usuário insere o nome do vinho: Chileno
Usuário insere o tipo do vinho: branco
Usuário insere a quantidade: 5
Usuário escolhe a opção 2.
Usuário insere o nome a ser buscado: Chileno
Programa imprime: branco
Programa imprime: 5
Usuário escolhe a opção 3.
Usuário insere o tipo a ser buscado: tinto
Programa imprime: 23
Usuário escolhe a opção 4.
Programa imprime: 28
Usuário escolhe a opção -1.
Programa termina.

#########################################
Teste Avaliativo 06

Problema

Faça um programa em Python que simule um experimento para análise da eficácia de uma vacina de COVID-19. Ao iniciar o programa, o usuário deve informar o número de participantes do experimento, seguido do perfil de cada participante. Em seguida, o usuário pode escolher as seguintes opções: (1) relatório de caracterização da população, (2) relatório de eficácia geral da vacina, (3) relatório de eficácia da vacina por gênero, (4) relatório de eficácia da vacina por faixa etária, (5) sair do programa. Ao final de qualquer opção entre 1 e 4, o programa deve aguardar a próxima opção. O programa só termina a execução quando o usuário escolher a opção 5.

Entrada:

Um inteiro N que indica o número de participantes do experimento seguido de N linhas onde cada linha contém o perfil de cada um dos participantes. O perfil de cada participante contém os seguintes dados separados por vírgula: genero (masculino: "M"; feminino: "F"), idade (número inteiro), grupo (vacina: "V"; placebo: "P") e se contraiu COVID (com COVID: "S"; sem COVID: "N"). Por exemplo, um participante do gênero feminino, com 34 anos, do grupo que recebeu a vacina e que não contraiu COVID seria representada por uma linha "F,34,V,N". A partir desse momento, o sistema está pronto para o uso, e aguarda um número de 1 a 5 indicando a opção escolhida pelo usuário. Enquanto o número 5 não for escolhido, o sistema aguardará novas opções ao término da execução da opção anterior. As opções não têm entrada de dados adicionais.

Saída:

As opções 1 a 4 apresentam as seguintes saídas:

Opção 1: na primeira linha, os percentuais de participantes do gênero masculino e feminino, separados por vírgula. Na segunda linha os percentuais de jovens, adultos e idosos, separados por vírgula. Na terceira linha, os percentuais de participantes que receberam vacina e placebo, separados por vírgula. Na quarta linha, os percentuais de participantes que contrairam e não contraíram COVID, separados por vírgula.
Opção 2: o percentual de eficácia geral da vacina. A eficácia da vacina deve ser calculada pela fórmula "100 * (a - b) / a", onde "a" representa todos os participantes que receberam placebo e foram infectados e "b" representa dodos os participantes que receberam a vacina e ainda assim foram infectados.
Opção 3: um percentual de eficácia por linha, onde a primeira linha restringe a população somente aos participantes do gênero masculino e a segunda linha restringe a população somente aos participantes do gênero feminino.
Opção 4: um percentual de eficácia por linha, onde a primeira linha restringe a população somente aos participantes jovens, a segunda linha restringe a população somente aos participantes adultos e a terceira linha restringe a população somente aos participantes idosos.
As faixas etárias consideradas são jovens de 0 a 19 anos, adultos de 20 a 59 anos e idosos a partir de 60 anos. Todos os percentuais fracionados, deve ter somente a sua parte inteira exibida (ex: 12,34% deve ser exibido como 12%).

Exemplos:

Entrada	Saída
10
F,12,V,N
F,43,V,N
F,65,V,N
M,35,V,N
M,86,V,S
F,34,P,S
M,62,P,S
M,15,P,S
F,38,P,N
M,14,P,N
1
5	50%,50%
30%,40%,30%
50%,50%
40%,60%
10
F,12,V,N
F,43,V,N
F,65,V,N
M,35,V,N
M,86,V,S
F,34,P,S
M,62,P,S
M,15,P,S
F,38,P,N
M,14,P,N
2
5	66%
10
F,12,V,N
F,43,V,N
F,65,V,N
M,35,V,N
M,86,V,S
F,34,P,S
M,62,P,S
M,15,P,S
F,38,P,N
M,14,P,N
3
5	50%
100%
10
F,12,V,N
F,43,V,N
F,65,V,N
M,35,V,N
M,86,V,S
F,34,P,S
M,62,P,S
M,15,P,S
F,38,P,N
M,14,P,N
4
5	100%
100%
0%
Observações:

No run.codes nunca passe uma string como parâmetro para a função input, pois internamente o input daria um print com essa string, e comprometeria a interpretação da saída do programa.
Use input().strip() para fazer a leitura de entrada, para evitar que espaços ou caracteres de controle antes ou depois do texto influenciem os resultados.
O run.codes somente considera um programa como correto se a saída for exatamente a esperada.

#########################################
Teste Avaliativo 07

Problema

Faça um programa em Python que permita análises de autonomia de diferentes automóveis sob diferentes condições de transito (urbano e rodoviário). A autonomia indica quantos kilometros o carro é capaz de percorrer com um litro de combustível em uma determinada condição de trânsito. Para cada automóvel, são feitas três medições em cada uma das condições de trânsito. Ao iniciar o programa, o usuário pode escolher as seguintes opções: (1) cadastrar um novo automóvel, (2) exibir a autonomia média geral, (3) listar os automóveis em ordem decrescente de autonomia média, (4) listar os automóveis em ordem crescente de autonomia média considerando somente trânsito urbano, (5) exibir o número de automóveis que têm ao menos uma medida de autonomia em transito urbano maior que alguma medida de autonomia em trânsito rodoviário. Ao final de qualquer opção entre 1 e 5, o programa deve aguardar a próxima opção. O programa só termina a execução quando o usuário escolher a opção 6.

Entrada:

Ao iniciar, o sistema espera a entrada de um número de 1 a 6 indicando a opção escolhida pelo usuário. Enquanto o número 6 não for escolhido, o sistema aguardará novas opções ao término da execução da opção anterior. A única opção que tem entrada adicional é a 1. Ao escolher a opção 1, o usuário informa os seguintes dados separados por ponto e vírgula: o modelo do automóvel (string), três medidas da sua autonomia em trânsito urbano e três medidas da sua autonomia em transito rodoviário. Cada medida é um número real em km / litro). Por exemplo, um automóvel Honda Civic com autonomias de 8.2, 10.1 e 9.3 km/l em transito urbano e 14.6, 12.5 e 13.4 km/l em transito rodoviário seria representado por uma linha contendo a seguinte informação: "Honda Civic;8.2;10.1;9.3;14.6;12.5;13.4".

Saída:

As opções 2 a 5 apresentam as seguintes saídas:

Opção 2: um número real que representa a autonomia média considerando todas as medições de todos os automóveis cadastrados em todas as condições de trânsito.
Opção 3: modelos dos automóveis, um por linha, ordenados decrescentemente pela autonomia média, considerando tanto trânsito urbano quanto rodoviário.
Opção 4: modelos dos automóveis, um por linha, ordenados crescentemente pela autonomia média, considerando somente trânsito urbano.
Opção 5: um número inteiro que representa a quantidade de automóveis que têm ao menos uma medida de autonomia em trânsito urbano maior que alguma medida de autonomia em trânsito rodoviário.
Todos os números reais de entrada e saída devem ter somente uma casa decimal.

Exemplos:

Entrada	Saída
1
Honda Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
GM Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Toyota Prius;15.0;14.0;18.0;17.0;22.0;21.0
2
6	11.9
1
Honda Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
GM Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Toyota Prius;15.0;14.0;18.0;17.0;22.0;21.0
3
6	Toyota Prius
Honda Civic
GM Opala
1
Honda Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
GM Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Toyota Prius;15.0;14.0;18.0;17.0;22.0;21.0
4
6	GM Opala
Honda Civic
Toyota Prius
1
Honda Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
GM Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Toyota Prius;15.0;14.0;18.0;17.0;22.0;21.0
5
6	1

Observações:

No run.codes nunca passe uma string como parâmetro para a função input, pois internamente o input daria um print com essa string, e comprometeria a interpretação da saída do programa.
Use input().strip() para fazer a leitura de entrada, para evitar que espaços ou caracteres de controle antes ou depois do texto influenciem os resultados.
O run.codes somente considera um programa como correto se a saída for exatamente a esperada.

#########################################
Teste Avaliativo 08

Problema

Faça um programa em Python que simule a análise de uma eleição. Ao iniciar o programa, o usuário deve informar o nome de cada candidato separado por vírgulas. Em seguida, o usuário deve informar qual operação ele deseja fazer, dentre as seguintes: (1) registrar votos de uma seção eleitoral, (2) listar o total de votos de cada seção eleitoral, (3) listar o total de votos recebidos por cada candidato, (4) listar os candidatos em ordem decrescente do número de votos recebidos, (5) indicar se terá segundo turno e (6) sair do programa. Ao final de qualquer operação entre 1 e 5 o programa deve aguardar a próxima operação. O programa só termina a execução quando o usuário escolher a operação 6.

Entrada:

Os nomes dos candidatos separados por vírgula. A partir desse momento, o sistema está pronto para o uso, e aguarda um número de 1 a 6 indicando a operação a ser realizada. Enquanto o número 6 não for escolhido, o sistema aguardará novas operações ao término das operações anteriores. A operação 1 tem como entrada as quantidades de votos de cada candidato, separadas por vírgula. A ordem deve ser a mesma usada para informar os nomes dos candidatos. As demais operações, de 2 a 6, não têm entrada de dados.

Saída:

As operações 2 a 5 apresentam as seguintes saídas:

Operação 2: números inteiros, um por linha, indicando o total de votos de cada seção, na mesma ordem que as seções foram registradas via opção 1.
Operação 3: números inteiros, um por linha, indicando o total de votos de cada candidato, na mesma ordem usada para informar os nomes dos candidatos.
Operação 4: nomes dos candidatos, um por linha, em ordem decrescente do número de votos recebidos pelos candidatos.
Operação 5: "Terá segundo turno." caso o candidato em 1o. lugar não some mais de 50% dos votos. "Não terá segundo turno." caso contrário.
Exemplos:

Entrada	Saída
João,Pedro,Paulo
1
30,20,10
1
10,50,40
2
6	60
100
João,Pedro,Paulo
1
30,20,10
1
10,50,40
3
6	40
70
50
João,Pedro,Paulo
1
30,20,10
1
10,50,40
4
5
6	Pedro
Paulo
João
Terá segundo turno.
Observações:

No run.codes NUNCA passe ums string como parâmetro para a função input, pois internamente o input daria um print com essa string, e comprometeria a interpretação da saída do programa.
O run.codes somente considera um programa como correto se a saída for exatamente a esperada.

#########################################













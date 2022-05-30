#ABERTURA DOS ARQUIVOS DE TEXTO
automato = open("automato.txt", "r")
entrada = open("entrada.txt", "r")
saida = open("saida.txt", "w")

#ESTADOS
estados = automato.readline().split()

#ALFABETO
alfabeto = automato.readline().split()

#ESTADO INICIAL
estadoInicial = automato.readline().split()

#ESTADOS FINAIS
estadosFinais = automato.readline().split()

#MATRIZ
matriz = []
x = automato.readline().split()
while len(x) > 0:
    linha = []
    for i in x:
        i = i.split(",")
        linha.append(i)
    matriz.append(linha)
    x = automato.readline().split()

#ENTRADAS
entradas = []
linha = entrada.readline().rstrip()
while len(linha) > 0:
    entradas.append(linha)
    linha = entrada.readline().rstrip()

#Caminhando Linha entrada
for linhaEntrada in entradas:
    copias = estadoInicial
    
    #Caminhando digito linha entrada
    for digitoLinhaEntrada in linhaEntrada:
        #Descobrir valor coluna
        valorColuna = alfabeto.index(digitoLinhaEntrada)
        
        copiasNova = copias.copy()
        #Caminhando copias
        for valorIndexCopia, valorCopia in enumerate(copias):
                      
            #Descobrir valor linha
            valorLinha = estados.index(valorCopia)

            atual = matriz[valorLinha][valorColuna]

            #Verificar se posição na matriz não é nulo
            if atual.count("*") == 0:
                
                #Verificar se posição na matriz é de apenas um estado
                if len(atual) == 1:
                    copiasNova[valorIndexCopia] = atual[0]
                
                else:
                    for valorIndexAtual, valorAtual in enumerate(atual):
                        if valorIndexAtual == 0:
                            copiasNova[valorIndexCopia] = valorAtual
                        else:
                            copiasNova.append(valorAtual)
            #if matriz[valorLinha][len(alfabeto)]!="*":
            #    print("tem o numero 3")
            if matriz[valorLinha][len(alfabeto)][0] != "*":
                copiasNova.append(matriz[valorLinha][len(alfabeto)][0])         
        copias = []                    
        copias = copiasNova
        
    if copias.index(estadosFinais[0]):
        saida.write("ACEITO\n")
    else:
        saida.write("NEGADO\n")

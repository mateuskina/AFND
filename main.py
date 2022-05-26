#ABERTURA DOS ARQUIVOS DE TEXTO
automato = open("automato.txt", "r")
entrada = open("entrada.txt", "r")

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

print()
print("Entrada: " + str(estados))
print("Alfabeto: " + str(alfabeto))
print("Estado Inicial: " + str(estadoInicial))
print("Estados Finais: " + str(estadosFinais))
print("Matriz: ")
for i in matriz:
    print(i)
print("Entradas: " + str(entradas))

#Caminhando Linha entrada
for linhaEntrada in entradas:
    copias = estadoInicial
    
    #Caminhando digito linha entrada
    for digitoLinhaEntrada in linhaEntrada:
        print("Simbolo lido: ",digitoLinhaEntrada)
        #Descobrir valor coluna
        valorColuna = alfabeto.index(digitoLinhaEntrada)
        
        copiasNova = copias.copy()
        #Caminhando copias
        for valorIndexCopia, valorCopia in enumerate(copias):
                      
            #Descobrir valor linha
            valorLinha = estados.index(valorCopia)

            print("Valor linha: ",valorLinha)
            print("valor coluna: ",valorColuna)
            atual = matriz[valorLinha][valorColuna]
            print("Valor matriz: ",atual)

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
                            print("copias novas",copiasNova)
            #if matriz[valorLinha][len(alfabeto)]!="*":
            #    print("tem o numero 3")
            if matriz[valorLinha][len(alfabeto)][0] != "*":
                copiasNova.append(matriz[valorLinha][len(alfabeto)][0])         
        copias = []                    
        copias = copiasNova
        
        print("Copias: ",copias)                    
    if copias.index(estadosFinais):
        saida.write("ACEITO\n")
    else:
        saida.write("NEGADO\n")
                




        print("------------------")
        print("")
    print(copias)

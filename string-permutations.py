from itertools import product
import string
import dados

matriz1 =   [[0,0,0,1],
            [5,0,3,0],
            [0,0,0,8],
            [3,2,0,0]]
matriz2 =  [[0,3,0,4],
            [1,0,2,0],
            [0,2,0,0],
            [4,0,2,0]]

matriz3 =[
[  0, 50,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#1
[  0,  0,215,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#2
[  0,215,  0, 85,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#3
[  0,  0, 85,  0,140,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 45,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#4
[  0,  0,  0,  0,  0,100,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 85,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#5
[  0,  0,  0,  0,  0,  0,125,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#6
[  0,  0,  0,  0,  0,  0,  0, 75,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#7
[  0,  0,  0,  0,  0,  0, 75,  0, 90,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#8
[  0,  0,  0,  0,  0,  0,  0, 90,  0,110,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#9
[  0,  0,  0,  0,  0,  0,  0,  0,110,  0, 85,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#10
[  0,  0,  0,  0,  0,  0,  0,  0,  0, 85,  0, 90,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#11
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,120,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#12
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,120,  0,135,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#13
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 80,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,120,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#14
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,140,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#15
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 60,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 50,  0,  0,  0,  0,  0,  0,  0,  0],#16
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 40,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 50,  0,  0,  0,  0,  0,  0,  0,  0],#17
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 60,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#18
[155,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 30],#19
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#20
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,120,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,100,  0],#21
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#22
[  0,  0,100,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 15,  0, 80,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,100,  0,  0,  0,  0],#23
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 85,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#24
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,100,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,  0,  0,  0],#25
[  0,  0,  0,  0,  0, 85,  0,125,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#26
[  0,  0,  0,  0,  0,  0,  0,  0,130,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 80,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#27
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,  0,  0],#28
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,  0,  0,  0,  0,  0,  0,  0,  0, 80,  0,  0],#29
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,135,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#30
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,120,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 85,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#31
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,100,  0, 90,  0,  0,  0,  0,  0,  0,  0],#32
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,  0,  0,  0,  0,  0],#33
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 60,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 80,  0,  0,  0,  0,  0],#34
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 15, 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],#35
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,100,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,  0,  0],#36
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,100,  0,  0,  0, 90,  0,  0],#37
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 90,  0,100,  0,  0,  0,  0,  0,  0,  0],#38
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 50,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 80,  0,  0,  0,  0,  0,  0, 50],#39
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]#40
]

alfabeto = list(string.ascii_uppercase)

#vertices = alfabeto[:len(matriz1)]
vertices = list(range(len(matriz1[0])))
arestas = []
i = 0
while i < len(matriz1):
    j = 0
    while j < len(matriz1[i]):
        if(matriz1[i][j]!=0 and matriz1[i][j] != matriz1[j][i]):
            arestas.append([i,j, False])
        if(matriz1[i][j]!=0 and matriz1[i][j] == matriz1[j][i]):
            arestas.append([i,j, True])
        j = j + 1
    i = i + 1

print(arestas)
def construirGrafo():
    print('ok')

grafo = dados.data[3]
#arestas = grafo["arestas"]
#vertices = alfabeto[:len(matriz1)]
#print(vertices)
caminhos = list(product(vertices, repeat=8))

#verifica se aresta ?? n??o direcionada e se j?? foi visitada em outra dire????o
def nao_direcionada_visitada(caminho, verticeInicial, verticeFinal):
    #colocar codigo aqui
    retorno = False
    if(existe_aresta(verticeFinal, verticeInicial)):
        i = 1
        while i < len(caminho):
            if(verticeFinal==caminho[i-1] and verticeInicial==caminho[i]):
                retorno = True
            i = i + 1
    return retorno  

#verifica se existe essa aresta
def existe_aresta(verticeInicial, verticeFinal):
    for aresta in arestas:
        if(aresta[0]==verticeInicial and aresta[1]==verticeFinal):
            return True
    return False


# verifica se existem arestas entre dois v??rtices
def verifica_aresta_vertice(caminho):
    i = 1
    arestasValidas = True
    while i < len(caminho):
        if existe_aresta(caminho[i-1],caminho[i]) == False:
            arestasValidas = False
            break
        i = i + 1
    if(arestasValidas):
        verifica_todas_arestas(caminho)



#verifica se visitou todas as arestas
def verifica_todas_arestas(caminho):
    faltaAresta = True
    for aresta in arestas:
        i = 1
        faltaAresta = True
        arestaFaltante = None
        while i < len(caminho):
            if(aresta[0]==caminho[i-1] and aresta[1]==caminho[i]):
                faltaAresta = False
                arestaFaltante = None
                break
            arestaFaltante = aresta
            i = i + 1
        if(arestaFaltante!=None):
            #colocar c??digo aqui
            if(nao_direcionada_visitada(caminho, arestaFaltante[0], arestaFaltante[1]) and arestaFaltante[2]):
                faltaAresta = False
        if(faltaAresta):
            break
    if(faltaAresta==False):
        print(caminho)

for caminho in caminhos:
    caminho = list(caminho)
    if caminho[0] != caminho[len(caminho)-1]:
        caminho.append(caminho[0])
    verifica_aresta_vertice(list(caminho))
    #print(caminho)





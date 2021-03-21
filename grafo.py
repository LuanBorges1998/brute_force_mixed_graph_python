from itertools import product # Biblioteca que realiza arranjos de análise combinatória
import time

# Classe que representa o grafo e realiza todas as operações com ele
class Grafo:
    # Método que inicializa a classe
    def __init__(self, matriz):
        self.matriz = matriz
        self.tamanhoCaminho = 0
        self.construirGrafo()   
        self.solucionado = False
        self.caminhosEncontrados = []
        self.inicio = 0
        self.fim = 0

    # Método onde percorre a matriz e constrói a lista de vértices e self.arestas
    def construirGrafo(self):
        self.vertices = list(range(len(self.matriz[0])))
        self.arestas = []
        qtdOrdenadas = 0
        qtdNOrdenadas = 0
        i = 0
        while i < len(self.matriz):
            j = 0
            while j < len(self.matriz[i]):
                if((self.matriz[i][j]!=0) and (self.matriz[i][j] == self.matriz[j][i])):
                    self.arestas.append([i,j, self.matriz[i][j], True])
                    qtdNOrdenadas = qtdNOrdenadas + 1
                if((self.matriz[i][j]!=0) and (self.matriz[i][j] != self.matriz[j][i])):
                    self.arestas.append([i,j, self.matriz[i][j], False])
                    qtdOrdenadas = qtdOrdenadas + 1
                j = j + 1
            i = i + 1
        print(self.arestas)
        self.tamanhoCaminho = qtdOrdenadas + int(qtdNOrdenadas/2)

    # Método que inicia o caminhamento no grafo
    def caminharGrafo(self):
        self.inicio = time.time()
        while(self.solucionado == False):
            #self.caminhos = list(product(self.vertices, repeat=self.tamanhoCaminho))
            for caminho in product(self.vertices, repeat=self.tamanhoCaminho):
                caminho = list(caminho)
                if caminho[0] != caminho[len(caminho)-1]:
                    caminho.append(caminho[0])
                self.verifica_aresta_vertice(list(caminho))
            self.tamanhoCaminho = self.tamanhoCaminho + 1
        self.calculaCusto()

    #verifica se aresta é não direcionada e se já foi visitada em outra direção
    def nao_direcionada_visitada(self, caminho, verticeInicial, verticeFinal):
        retorno = False
        if(self.existe_aresta(verticeFinal, verticeInicial)):
            i = 1
            while i < len(caminho):
                if(verticeFinal==caminho[i-1] and verticeInicial==caminho[i]):
                    retorno = True
                i = i + 1
        return retorno  

    #verifica se existe essa aresta
    def existe_aresta(self, verticeInicial, verticeFinal):
        for aresta in self.arestas:
            if(aresta[0]==verticeInicial and aresta[1]==verticeFinal):
                return True
        return False

    # verifica se existem self.arestas entre dois vértices
    def verifica_aresta_vertice(self, caminho):
        i = 1
        arestasValidas = True
        while i < len(caminho):
            if self.existe_aresta(caminho[i-1],caminho[i]) == False:
                arestasValidas = False
                break
            i = i + 1
        if(arestasValidas):
            self.verifica_todas_arestas(caminho)



    #verifica se visitou todas as self.arestas
    def verifica_todas_arestas(self, caminho):
        if caminho == [0, 1, 2, 0]:
            print('ok')
        faltaAresta = True
        for aresta in self.arestas:
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
                if(self.nao_direcionada_visitada(caminho, arestaFaltante[0], arestaFaltante[1]) and arestaFaltante[3]):
                    faltaAresta = False
            if(faltaAresta):
                break
        if(faltaAresta==False):
            self.solucionado = True
            self.caminhosEncontrados.append(caminho)

    # Método que calcula o custo dos caminhos encontrados e imprime o melhor
    def calculaCusto(self):
        melhorCaminho = []
        melhorCusto = 0
        for caminhoEncontrado in self.caminhosEncontrados:
            i = 1
            custoCaminho = 0
            while i < len(caminhoEncontrado):
                custoCaminho = custoCaminho + self.matriz[caminhoEncontrado[i-1]][caminhoEncontrado[i]]
                i = i + 1
            if((melhorCusto==0) or (custoCaminho<melhorCusto)):
                melhorCusto = custoCaminho
                melhorCaminho = caminhoEncontrado
        print('Melhor caminho: '+str(melhorCaminho))
        print('Menor custo: '+str(melhorCusto))
        self.fim = time.time()
        print(self.fim - self.inicio)

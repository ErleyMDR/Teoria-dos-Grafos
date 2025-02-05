
class Grafo:
    def __init__(self):
        self.lista_de_adjacencia = {}
        
    def add_vertice(self,v):
        if v not in self.lista_de_adjacencia:
            self.lista_de_adjacencia[v] = []
    
    def add_aresta(self,v ,u , p = 1):
        self.add_vertice(v)
        self.add_vertice(u)
        self.lista_de_adjacencia[v].append((u,p))
    
    def num_vertices(self):
        return len(self.lista_de_adjacencia)
    
    def num_arestas(self):
        l = []
        for k in list(self.lista_de_adjacencia.values()):
            l.append(len(k))
        return sum(l)/2
    
    def vizinhaca(self,v):
        l = []
        for i in range(len(self.lista_de_adjacencia[v])):
            l.append(self.lista_de_adjacencia[v][i][0])
        return l
    
    def grau_do_vertice(self,v):
        return len(self.lista_de_adjacencia[v])
    
    def peso_da_aresta(self,v,u):
        for i in range(len(self.lista_de_adjacencia[v])):
           if u == self.lista_de_adjacencia[v][i][0]:
               return self.lista_de_adjacencia[v][i][1]
        return 0
    
    def min_grau(self):
        l =  []
        for k in list(self.lista_de_adjacencia.keys()):
            l.append(len(self.lista_de_adjacencia[k]))
        return min(l)
    
    def max_grau(self):
        l =  []
        for k in list(self.lista_de_adjacencia.keys()):
            l.append(len(self.lista_de_adjacencia[k]))
        return max(l)
    
    def bfs(self,v):
        visitados = set()
        visitados.add(v)
        distancia = {v : 0}
        pais = [(v,v)]
        fila = [v]
        while len(visitados) != len(self.lista_de_adjacencia):
            for n in range(len(self.lista_de_adjacencia[fila[0]])):
                if self.lista_de_adjacencia[fila[0]][n][0] not in visitados:
                    visitados.add(self.lista_de_adjacencia[fila[0]][n][0])
                    fila.append(self.lista_de_adjacencia[fila[0]][n][0])
                    pais.append((self.lista_de_adjacencia[fila[0]][n][0],fila[0]))
                    distancia[self.lista_de_adjacencia[fila[0]][n][0]] = distancia[fila[0]]+1
            fila.pop(0)
            
        return distancia, pais
    
    def dfs(self, vertice):
        visitados = set()  #inicia conjunto dos vértices que já foram visitados
        tempo_inicial = {}  #dictionary para armazenar o tempo inicial de cada um dos vértices
        tempo_final = {}  #dictionary para armazenar o tempo em que acaba a busca do vertice e de seus vizinhos, exceto pai
        pais = {}  #dict para armazenar o pai de cada vertice
        tempo = 0  #inicia contador de tempo em 0
        pilha = []  #lista usada como pilha para controlar a ordem dos vértices que vão ser visitados
        #adiciona o vértice inicial à pilha e define seu pai como None
        pilha.append(vertice)  #começa a busca empilhando o vértice inicial
        pais[vertice] = vertice  #define que o vértice inicial não tem pai

        #laço que percorre a pilha inteira, até não sobrar vertices
        while pilha:
            v = pilha[-1]  #atribui a "v" o ultimo vertice da lista

            if v not in visitados: #se "v" não foi visitado
                visitados.add(v)  #marca "v" como visitado
                tempo += 1  #aumenta o tempo depois de visitar "v"
                tempo_inicial[v] = tempo  #registra o tempo inicial que o vertice v foi descoberto

                #itera em cada vértice adjacente a "v" na lista de adjacência
                for adjacente in self.lista_de_adjacencia[v]:
                    u = adjacente[0]  #pega o vértice adjacente "u" 
                    if u not in visitados:  #se "u" ainda não foi visitado
                        pais[u] = v  #define "v" como pai de "u" na árvore de DFS
                        pilha.append(u)  #adiciona "u" à pilha para ser visitado mais tarde

            else:#se "v" já foi visitado 
                pilha.pop()  #tira "v" do topo da pilha
                if v not in tempo_final:  #se o tempo final de "v" ainda não está no dict tempo_final
                    tempo += 1  #aumenta em 1 o tempo ao terminar a visitação do vértice "v"
                    tempo_final[v] = tempo  #registra o tempo final em que a visita do vértice "v" terminou

        #retorna 3 dict: um com o tempo inicial, outro tempo final e outro os pais dos vértices
        return tempo_inicial,tempo_final,pais
    
    def bellman_ford(self, vertice):
        dist = [float("Inf" )] * self.num_vertices() # inicializa uma lista que considera como infinito a distância dos vértices em relação a origem
        dist[vertice - 1] = 0 # define como zero a distância da origem, já que é em relação a ela mesmo
        vertices = [0] * self.num_vertices() # inicializa a lista de vértices, serve para visualizar melhor quem é o pai de quem, e qual o vértice que se refere a lista de distâncias
        vertices[vertice - 1] = vertice # define o valor do vertice de origem na sua posição
        pais = [0] * self.num_vertices() # inicializa a lista de pais
        pais[vertice - 1] = vertice # define a origem como pai dela mesma
        
        for i in range(self.num_vertices()):
            for valor in self.lista_de_adjacencia[i + 1]: # percorre os vizinhos de cada vertice
                u, v, p = i + 1, valor[0], valor[1]
                if dist[u-1] != float("Inf") and dist[u-1] + p <= dist[v-1]: # confere quem tem a menor distância
                    dist[v-1] = dist[u-1] + p # atualiza a distância
                    vertices[v-1] = v 
                    pais[v-1] = u # atualiza o pai
        
        i = 0
        for valor in self.lista_de_adjacencia[i + 1]: 
            u, v, p = i + 1, valor[0], valor[1]
            i = i + 1
            if dist[u-1] != float("Inf") and dist[u-1] + p < dist[v-1]: # confere se tem ciclo negativo no grafo
                print("Grafo contém ciclo negativo.")
                return
 
        return vertices, dist, pais
    
    def dijkstra(self, vertice):
        dist = [float('inf')] * self.num_vertices()  #inicializa a lista de distâncias como infinito para todos os vértices
        dist[vertice - 1] = 0  #define a distância do vértice inicial como 0
        pais = [None] * self.num_vertices()  #inicializa a lista de pais para reconstruir o caminho mínimo, com valor None
        fila_de_prioridade = [(0, vertice)]  #cria uma lista para simular a fila de prioridade, inicializada com todos os vértices (preferi não usar a biblioteca heapq para deixar o codigo mais simples, além de não ter muita prática)
        processado = set()  #conjunto de vértices já processados para evitar reprocessamento

        while fila_de_prioridade:  #enquanto tiver vertices a serem processados
            fila_de_prioridade.sort()   #ordena a lista pela distância
            d, u = fila_de_prioridade.pop(0) #remove e retorna o vértice com a menor distância da fila
            if u in processado:  #se o vertice for processado, pula para o proximo loop
                continue

            processado.add(u)# marca como processado

            for v, p in self.lista_de_adjacencia[u]:  #itera sobre os vértices adjacentes a 'u'
                if dist[v - 1] > dist[u - 1] + p:  #se encontrar um caminho mais curto para o vértice 'v' através de 'u'
                    dist[v - 1] = dist[u - 1] + p  #atualiza a distância mínima encontrada para 'v'
                    pais[v - 1] = u  #atualiza o pai de 'v' para 'u' no caminho mínimo
                    fila_de_prioridade.append((dist[v - 1], v))  #insere o vértice 'v' na lista de fila_de_prioridade com a nova distância

        #retorna a lista de pais (predecessores) e as distâncias mínimas
        return pais, dist
    
    
            
        

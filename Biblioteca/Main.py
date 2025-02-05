from Grafo import Grafo

def Ler_Arquivo(path):
    A = open(path,'r')
    Arestas = []
    for linha in A.readlines():
        if linha[0] == 'a':
            linha = linha.split()
            Arestas.append((int(linha[1]),int(linha[2]),int(linha[3])))
    return Arestas

M = Ler_Arquivo("C:/Users/Lucas/Desktop/Coisas do Erley/Grafos/Biblioteca/USA-road-d.NY.gr")

G = Grafo()
   
for x in M:
    G.add_aresta(x[0],x[1],x[2])
    
print(G.bfs(1))



from Grafo import Grafo
from Digrafo import Digrafo

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
    
maior_grau = G.max_grau()
menor_grau = G.min_grau()


print("Item a.\nEste é o menor grau presente no grafo:", menor_grau,"\nUm vértice que possui este grau é:")
for i in G.lista_de_adjacencia.keys():
    if len(G.lista_de_adjacencia[i]) == menor_grau:
        print(i)
        break
print("Item b.\nEste é o maior grau presente no grafo:", maior_grau,"\nUm vértice que possui este grau é:")
for i in G.lista_de_adjacencia.keys():
    if len(G.lista_de_adjacencia[i]) == maior_grau:
        print(i)
        break


ver, dis, pai = G.bellman_ford(129)
maior_d = 0
for d in range(len(dis)):
    if dis[d] > maior_d and dis[d] != float("Inf"):
        maior_d = dis[d]
        vertice = d+1
print("Este é o vértice mais distante do vértice 129:", vertice, "\nEsta é a distância do vértice:", maior_d)

"""inf = float("Inf")

def Floyd_Warshall(m):
    num_v = len(m)
    
    for k in range(num_v):
        for j in range(num_v):
            for i in range(num_v):
                m[i][j] = min([m[i][j] , m[i][k]+m[k][j]])
    
    for n in m:
        print(n)
        
        
t = [[0,6,7,inf,inf],
     [inf,0,8,5,-4],
     [inf,inf,0,-3,9],
     [inf,-2,inf,0,inf],
     [2,inf,inf,7,0]]

a = [[0,1,inf,inf,inf,inf],
     [inf,0,1,3,2,inf],
     [3,inf,0,2,inf,inf],
     [inf,inf,inf,0,inf,2],
     [inf,inf,inf,-3,0,inf],
     [inf,inf,inf,inf,3,0]]

Floyd_Warshall(a)"""

l = "a 1 2 56"
a = []
b = l.split()
a.append((b[1],b[2],b[3]))
print(a)
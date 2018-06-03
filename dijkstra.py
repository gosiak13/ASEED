import math

#v= [a,b,c,d,e,f,g]
a = [0, math.inf, 1, 2, math.inf, math.inf, math.inf]
b = [math.inf, 0, 2, math.inf, math.inf, 3, math.inf]
c = [1, 2, 0, 1, 3, math.inf, math.inf]
d = [2, math.inf, 1, 0, math.inf, math.inf, 1]
e = [math.inf, math.inf, 3, math.inf, 0, 2, math.inf]
f = [math.inf, 3, math.inf, math.inf, 2, 0, 1]
g = [math.inf, math.inf, math.inf, 1, math.inf, 1, 0]

nodes = [a,b,c,d,e,f,g]

def dijkstra(nodes):
    open = [1,1,1,1,1,1,1]
    closed = [0,0,0,0,0,0,0]
    outreach = nodes[0].copy()
    outreach2 = nodes[0].copy()
    open[0] = 0
    closed[0] = 1
    outreach[0] = math.inf

    #for i in range(4):
    while (0 in closed):
        closest = min(outreach)
        #print(closest)
        index_of_closest = outreach.index(closest)
        print(index_of_closest)
        outreach[outreach.index(closest)] = math.inf
        open[index_of_closest] = 0
        closed[index_of_closest] = 1
        for i in range (len(outreach)):
            if ((nodes[index_of_closest][i] + closest) < outreach2[i]):
                outreach2[i] = nodes[index_of_closest][i] + closest
                if (open[i] == 1) :
                    outreach[i] = nodes[index_of_closest][i] + closest

    print (outreach2)


# Dijkstra(G,w,s):
#    dla każdego wierzchołka v w V[G] wykonaj
#       d[v] := nieskończoność
#       poprzednik[v] := niezdefiniowane
#    d[s] := 0
#    Q := V
#    dopóki Q niepuste wykonaj
#       u := Zdejmij_Min(Q)
#       dla każdego wierzchołka v – sąsiada u wykonaj
#          jeżeli d[v] > d[u] + w(u, v) to
#             d[v] := d[u] + w(u, v)
#             poprzednik[v] := u
#
#    Wyświetl("Droga wynosi: " + d[v])

dijkstra(nodes)
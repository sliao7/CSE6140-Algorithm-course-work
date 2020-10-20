from graph import graph
import heapq
from collections import deque,defaultdict
import time

## This is the workplace I used to design and test functions in run_experiments.py

def parse_edges(filename):
        # Write this function to parse edges from graph file to create your graph object
        f = open(filename, "r")
        n_vertices, n_edges = f.readline().split(' ')
        n_vertices, n_edges = int(n_vertices), int(n_edges)

        G = graph()
        new_edge = f.readline()
        while new_edge:
            new_edge = new_edge.split(' ')
            frm, to, weight = int(new_edge[0]), int(new_edge[1]), int(new_edge[2])
            G.add_edge(frm, to, weight)
            new_edge = f.readline()
        return G
        
 # use a small graph to test the functions. It is the graph in CSE 6140 slides-09-01 page 34
g = parse_edges('small_graph.txt')
# can play around with g
# v2 = g.get_vertex(2)
# print([v.id for v in v2.get_connections()])
# print(g.num_vertices)
# print(g.num_edges)
# print(g.get_vertices())
# print(heapq.heapify([1,2,3]))



def computeMST(G):
    S = set() # contains seen vertices
    num_vertices = G.num_vertices
    min_weight = [float('inf')]*num_vertices  
    previous = [None]*num_vertices 
    mst = graph() # initialize the MST

    Q = [(min_weight[0],0)] 
    Qset = set([0])   
    heapq.heapify(Q)
    while Q:
        weight, u = heapq.heappop(Q)
        if u in S:
            continue
        S.add(u)

        # Add u and its smallet edge to MST
        mst.add_vertex(u) if weight == float('inf') else mst.add_edge(u,previous[u],weight)

        u = G.get_vertex(u)
       
        for v in u.get_connections():
            if v.id not in S:
                if u.get_weight(v) < min_weight[v.id] :
                    min_weight[v.id] = u.get_weight(v)
                    previous[v.id] = u.id
                heapq.heappush(Q,(min_weight[v.id], v.id))
                 
    # return the sum of the weights of the MST and the MST
    
    return sum(min_weight[1:]), mst


    
# mst, _ = computeMST(g)
# print(mst)
   
    
def max_edge(u,v,MST):
    # u, v: int
    # MST: graph
    # find the max weighted edge in the path connecting u and v in MST using BFS
    seen = set([u])
    queue = deque([u])
    parent = defaultdict()
    while queue:
        node = queue.popleft() # node type: 
        node = MST.get_vertex(node) # node type: vertex
        for vv in node.get_connections(): # vv type: vertex
            if vv.id not in seen:
                seen.add(vv.id)
                parent[vv.id] = node.id
                if vv.id != v:               
                    queue.append(vv.id) 
                else:
                    queue = []
                    break
   
    max_weight = 0
    v1, v2 = None, None
    while v != u:
        new_weight = MST.get_vertex(v).get_weight(MST.get_vertex(parent[v]))
        if new_weight > max_weight:
            max_weight = new_weight
            v1, v2 = v, parent[v]
        v = parent[v]
        
    return v1, v2, max_weight # maximum edge in path(u,v)


def recomputeMST(u,v,weight,MST, MSTWeight):
    u1, v1, max_weight = max_edge(u,v,MST)
    if max_weight > weight: # need to add the new edge
        MST.remove_edge(u1,v1)
        MST.add_edge(u,v,weight)       
       
        MSTWeight = MSTWeight + weight - max_weight
    return MSTWeight, MST

    

def test(filename):
    g = parse_edges(filename + '.gr')
    output = open(filename + '.out', 'r')
    print('MST_weight from part(2): ', output.readline())
    extra = open(filename + '.extra','r')
    n = int(extra.readline())
    print('num of extra vertices: ', n)

    return g, extra, output, n

g, extra, output, n = test('../data/rmat0608') # this is how to access a parallel folder


mst_weight, mst = computeMST(g)
# check the answers
for i in range(n):
    extra_edge = list(map(lambda x: int(x), extra.readline().split(' ')))
    u, v, weight = extra_edge[0], extra_edge[1], extra_edge[2]
    
    mst_weight, mst = recomputeMST(u,v,weight,mst, mst_weight)
    
    if mst_weight != int(output.readline().split()[0]):
        print('The algorithm breakdown at the ', i, 'th new edge ', u, v, weight)
        break

print('Congratulaitons! Shasha passed all the test!')


# python3 run_experiments.py rmat0406.gr rmat0406.extra rmat0406.txt







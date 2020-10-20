from collections import deque,defaultdict
class vertex:
    def __init__(self,node):
        self.id = node
        self.adjacent = {} # vertex:weight

    def __str__(self):
        # for print out result
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight):
        # if an edge already exists, only add it when it has a smaller weight
        if neighbor in self.adjacent and weight > self.get_weight(neighbor):
            pass
        else:
            self.adjacent[neighbor] = weight

    def remove_neighbor(self, neighbor):
        if neighbor in self.adjacent:
            del self.adjacent[neighbor]

    def is_connected(self,neighbor):
        return neighbor in self.adjacent

    def get_connections(self):
        return list(self.adjacent.keys())

    def get_weight(self,neighbor):
        return self.adjacent[neighbor]


class graph:
    # weighted undirected graph
    # can be connected or not
    def __init__(self):
        self.vert_dict = {} # vertex_id (int) : vertex
        self.num_vertices = 0
        self.num_edges = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self,node):
        self.num_vertices += 1
        new_vertex = vertex(node)
        self.vert_dict[node] = new_vertex

    def get_vertex(self,node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        else:
            return None

    def add_edge(self, frm, to, weight):
        # for new vertices
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        if not self.vert_dict[frm].is_connected(self.vert_dict[to]):
            self.num_edges += 1

        self.vert_dict[frm].add_neighbor(self.vert_dict[to],weight)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm],weight)


    def remove_edge(self, frm, to):
        self.vert_dict[frm].remove_neighbor(self.vert_dict[to])
        self.vert_dict[to].remove_neighbor(self.vert_dict[frm])
        self.num_edges -= 1


    def get_vertices(self):
        # return a list of ints, the id of vertices
        return list(self.vert_dict.keys())


def max_edge(u,v,MST):
    # find the max weighted edge in the path connecting u and v in MST using BFS
    # u, v: integers, id of the vertices
    # MST: a tree graph where there is a unique path between u and v
    
    seen = set([u])   
    parent = defaultdict()

    # use BFS to find the path from u to v in MST
    queue = deque([u])
    while queue:

        node = queue.popleft() # type(node): int
        node = MST.get_vertex(node) # type(node): vertex

        for vv in node.get_connections(): # type(vv): vertex

            if vv.id not in seen:

                seen.add(vv.id)

                parent[vv.id] = node.id 

                if vv.id != v:               
                    queue.append(vv.id) 
                else:
                    # endpoint v is found
                    queue = []
                    break
    # track path back from v and find the edge with the maximum weight in the path
    max_weight = 0
    v1, v2 = None, None # vertices of the maximum edge

    # loop through the edges one by one in the path u-v, starting from v
    while v != u:
        # get the weight of current edge
        new_weight = MST.get_vertex(v).get_weight(MST.get_vertex(parent[v]))

        # check for the maximum edge
        if new_weight > max_weight:
            # update the maximum edge
            max_weight = new_weight
            v1, v2 = v, parent[v]
            
        # update current vertex
        v = parent[v]
        
    return v1, v2, max_weight # maximum edge in path(u,v)

def main():
    data = [(1,2,3.2), (3,4,2.3), (4,2,5.1), (3,4,1),(3,4,4)]
    g = graph()
    for frm, to, weight in data:
       g.add_edge(frm,to,weight)

    for v in g.get_vertices():
        print(v)
        print(g.get_vertex(v))

    print('Number of edges: ', g.num_edges)
    print('Number of vertices, ', g.num_vertices)
    print('The weight between 3 and 4 is ', g.get_vertex(3).get_weight(g.get_vertex(4)))

if __name__ == '__main__':
        main()







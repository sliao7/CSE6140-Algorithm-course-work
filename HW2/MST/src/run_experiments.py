#!/usr/bin/python
# CSE6140 HW2

# to run this file in termial go to dir MST and run: bash runTests.sh

import time
import sys
from graph import graph, max_edge
import heapq
from collections import deque,defaultdict


class RunExperiments:
    def parse_edges(self, filename):
        # parse edges from graph file to create your graph object
        # filename: string of the filename
        f = open(filename, "r")
        n_vertices, n_edges = f.readline().split(' ')
        n_vertices, n_edges = int(n_vertices), int(n_edges)

        G = graph() # create a graph

        # add edges to the graph
        new_edge = f.readline()
        while new_edge:
            new_edge = new_edge.split(' ')
            frm, to, weight = int(new_edge[0]), int(new_edge[1]), int(new_edge[2])
            G.add_edge(frm, to, weight)
            new_edge = f.readline()
        return G


    def computeMST(self, G):
        # compute total weight of MST
        # Prim's Algorithm implemented
        # G: graph object
        S = set() # contains seen vertices
        num_vertices = G.num_vertices

        # store the minimum weights
        min_weight = [float('inf')]*num_vertices  

        # track the parents of the vertices in the tree
        previous = [None]*num_vertices 
        mst = graph() # initialize the MST

        Q = [(min_weight[0],0)]    
        heapq.heapify(Q)


        while Q:

            weight, u = heapq.heappop(Q)

            if u in S:
                # S may contain visited nodes added before 
                continue

            S.add(u)

            # Add u and its smallet edge to MST
            mst.add_vertex(u) if weight == float('inf') else mst.add_edge(u,previous[u],weight)

            u = G.get_vertex(u) # u tpye: vertex

            for v in u.get_connections():
                if v.id not in S:
                    if u.get_weight(v) < min_weight[v.id]:
                        # find a smaller edge, update weights and parents
                        min_weight[v.id] = u.get_weight(v)
                        previous[v.id] = u.id

                    heapq.heappush(Q,(min_weight[v.id], v.id))
                 
        # return the sum of the weights of the MST and the MST
        return sum(min_weight[1:]), mst


    def recomputeMST(self,u,v,weight,MST, MSTWeight):
        # recompute the weight of the MST of G when new edge (u,v, weight) is added
        # u,v,weight (int): vertices and weight of the new edge
        # MST (int): minimum spanning tree of a connected graph G
        # MSTWeight: the total weight of MST

        u1, v1, max_weight = max_edge(u,v,MST) # get the largest edge in MST

        if max_weight > weight:
         # need to add the new edge and remove the largest edge
            MST.remove_edge(u1,v1)
            MST.add_edge(u,v,weight)       
            MSTWeight = MSTWeight + weight - max_weight

        return MSTWeight, MST

    def main(self):

        num_args = len(sys.argv)

        if num_args < 4:
            print("error: not enough input arguments")
            exit(1)

        graph_file = sys.argv[1]
        change_file = sys.argv[2]
        output_file = sys.argv[3]

        # Construct graph
        G = self.parse_edges(graph_file)

        start_MST = time.time()  # time in seconds
        # call MST function to return total weight of MST
        MSTweight, MST = self.computeMST(G)
        total_time = (time.time() - start_MST) * 1000  # to convert to milliseconds

        # Write initial MST weight and time to file
        output = open(output_file, 'w')
        output.write(str(MSTweight) + " " + str(total_time) + "\n")

        # Changes file
        with open(change_file, 'r') as changes:
            num_changes = changes.readline()

            for line in changes:
                # parse edge and weight
                edge_data = list(map(lambda x: int(x), line.split()))
                assert(len(edge_data) == 3)

                u, v, weight = edge_data[0], edge_data[1], edge_data[2]

                # call recomputeMST function
                start_recompute = time.time()
                MSTweight, MST = self.recomputeMST(u, v, weight, MST, MSTweight)
                
                # to convert to milliseconds
                total_recompute = (time.time() - start_recompute) * 1000

                # write new weight and time to output file
                output.write(str(MSTweight) + " " + str(total_recompute) + "\n")
                


if __name__ == '__main__':
    # run the experiments
    runexp = RunExperiments()
    runexp.main()

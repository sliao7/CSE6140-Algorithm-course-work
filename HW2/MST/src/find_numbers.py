import sys
# This file is to read the first lines of all the files in data folder and print out the number of
# vertices and edges in each dataset.
# To run this file, open terminal, go to dir MST, and run the following line:
# bash find_number.sh > output.txt

num_args = len(sys.argv)

if num_args < 3:
    print("error: not enough input arguments")
    exit(1)

graph_file = sys.argv[1]
change_file = sys.argv[2]


print(graph_file + '\n')
graph_file = open(graph_file,'r')
print('Number of vertices and edges: ' +  graph_file.readline() + '\n')
graph_file.close()

change_file = open(change_file,'r')
print('Number of extra edges: ' + change_file.readline() + '\n')
change_file.close()



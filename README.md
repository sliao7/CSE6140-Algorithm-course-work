# CSE6140-course-work
Include all the homework problems and projects for CSE 6140 Algorithm. 

## HW1 [report](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW1/report.pdf)
### 1. Big-O time Complexity
### 2. Algorithm Design and Complexity Analysis (Box Throwing)
### 3. Greedy - Points on a 2D plane

* Designed a Greedy algorithm that uses a minimum number of disks centered on a line to cover all n distinct points on 2D plane.

* Proved the optimality of the Greedy algorithm by induction.

* Space complexity: O(n)

* Time complexity: O(n log n)

### 4. Greedy - Why is the pool always so busy anyway?

* Designed a Greedy algorithm to produce a schedule of n athletes for the "Tech Swim Run Bike" Triathalon program at Georgia Tech to minimize the completion time.

* Proved the optimality of the Greedy algorithm by an exchange argument.

* Space complexity: O(n)

* Time complexity: O(n log n)

## HW2 [report](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/report.pdf)
### 1. Dynamic Programming: Atlanta MARTA
* Designed a DP algorithm [(code)](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/Python/dp_tickets.py) to find an n days purchase plan that minimizes the amount of money for a commuting plan.

* Time and space complexity O(n)

### 2. Dynamic Programming: Buy More 
* Designed a DP algorithm [(code)](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/Python/dp_buy_computers.py) to find an ordering plan for a manager of a consumer-electronic store to meet the n monthly demands with an inventory that can keep up to I computers, whilst minimizing the cost.

* Time and space complexity: O(nI) 

### 3. Minimum Spanning Tree [code](https://github.com/sliao7/CSE6140-Algorithm-course-work/tree/master/HW2/MST)

* Designed two data structuress, [**vertex** object and **graph** object](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/MST/src/graph.py) to make it very cheap (constant time) and convenient to add, search, and remove edeges in a graph.
#### Static Computation: find an MST and compute the cost
* Implemented Prim's Algorithm in the function [**computeMST**](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/MST/src/run_experiments.py) to find the MST and compute the cost of the MST in [given weighted graph data files](https://github.com/sliao7/CSE6140-Algorithm-course-work/tree/master/HW2/MST/data). 
#### Dynamic Recomputation: update the cost of the MST given new edges added
* Applied BFS in the function [**max_edge**](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/MST/src/graph.py) to find the maximum weighted edge between two vertices in a graph.
* Implemented the function [**recomputeMST**](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/MST/src/run_experiments.py) to computes the new MST given the new edge to be added into the graph.
#### Experiemtns: 
* Ran my code for all 13 input RMAT graphs [[1]](#1), which are synthetic graphs with power-low degree distributions and small-world characteristics. 
* The largest graph containes 65536 vertices and 7926934 edges.
#### Report:
* Analyzied theoretical complexity for the two algoritms **computeMST** and **recomputeMST** and compared the theoretical results with the experimental results. See the [report](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/report.pdf) on page 7.

## HW3[report](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW3/report.pdf)
### 1. Dominating set
* Problem: Given a large network of workstations modeled as a graph G, and a number k, is there a way to place k copies of the database at k different nodes so that every node either has a copy of the database or is connected by a direct link to a node that has a compy of the database?
* Proved that the Dominating Set Problem is NP-complete.

### 2. Frenemies
* Problem: Given a set of n friends and a set of the pairs of enemies, is there a way to create a seating plan to arrange this set of n frineds around a round table such that none of the two enemies will seat next to each other.
* Proved that the Frenemies Problem is NP-complete.

### 3. Let's go hiking
* Problem: Given a bag containning n items of different weights. Can we divide the items evenly into two groups so that each of them has the same amount of weight? Moreover, can we divide the items such tha the weight difference of items of the two groups is less than 10lbs.
* Proved both the two problems are NP-complete.

## References
<a id="1">[1]</a> 
D. Chakrabarti, Y. Zhan, and C. Faloutsos.
R-MAT: A Recursive Model for Graph Mining.
Proc. 4th SIAM Intl. Conf. on Data Mining.
Florida, USA, April 2004.


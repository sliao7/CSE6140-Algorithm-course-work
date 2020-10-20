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
* Designed a DP algorithm to find an n days purchase plan that minimizes the amount of money for a commuting plan.

* Time and space complexity O(n)

### 2. Dynamic Programming: Buy More
* Designed a DP algorithm to find an ordering plan for a manager of a consumer-electronic store to meet the n monthly demands with an inventory that can keep up to I computers, whilst minimizing the cost.

* Time and space complexity: O(nI) 

### 3. Minimum Spanning Tree [code](https://github.com/sliao7/CSE6140-Algorithm-course-work/tree/master/HW2/MST)

* Designed two data structuress, [**vertex** object and **graph** object](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/MST/src/graph.py) to make it very cheap (constant time) and convenient to add, search, and remove edeges in a graph.
#### Static Computation: find an MST and compute the cost
* Implemented Prim's Algorithm in the function [**computeMST**](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/MST/src/run_experiments.py) to find the MST and compute the cost of the MST in [given weighted graph data files](https://github.com/sliao7/CSE6140-Algorithm-course-work/tree/master/HW2/MST/data). 
#### Dynamic Recomputation: update the cost of the MST given new edges added
* Applied BFS in the function [**max_edge**](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/MST/src/graph.py) to find the maximum weighted edge between two vertices in a graph.
* Implemented the function [**recomputeMST**](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/MST/src/run_experiments.py) to computes the new MST given the new edge to be added into the graph.
#### Experiemtns: 
* ran my code for all 13 input RMAT graphs [[1]](#1), which are synthetic graphs with power-low degree distributions and small-world characteristics. 
#### Report:
* Analyzied theoretical complexity for the two algoritms **computeMST** and **recomputeMST** and compared the theoretical results with the experimental results. See the [report](https://github.com/sliao7/CSE6140-Algorithm-course-work/blob/master/HW2/report.pdf) on page 7.

## References
<a id="1">[1]</a> 
D. Chakrabarti, Y. Zhan, and C. Faloutsos.
R-MAT: A Recursive Model for Graph Mining.
Proc. 4th SIAM Intl. Conf. on Data Mining.
Florida, USA, April 2004.


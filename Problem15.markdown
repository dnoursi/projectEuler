## Lattice Paths
### Problem
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
### Solution

I solved this problem with a combinatoric sort of approach. We see that going from one corner an N x N lattice to the other requires going, in some order, N steps to the right and N steps down.
Upon inspection, I noticed the key which is that permutations on this series of steps correspond to distinct paths; indeed, this correspondence is bijective.

By applying our knowledge of such permutations, we can compute that an N x N lattice has (2N choose N) unique paths. 

40! / ((20!)^2) = 137846528820






# traveling-salesman-problem

## Question 1. 
H(σ) = Σ(σi, σi+1) + d(σm, σ1) | 1 <= i <= m-1 → #H(σ) = m
Since calculating the of a given configuration σ requires calculating "m" times the distance between two cities (see above) and the number of possible permutations is m!, the time spent calculating would be equal to (m).(m!).(time to calculate one distance)
Therefore, this algrithm has a time complexity of O(n!). See more in the output of question1.py.

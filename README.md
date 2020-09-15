# codeIT-challenge-2020
A small algorithm variation on 0-1 Knapsack problem.

## The problem

Subset Sums Problem
Given an array of integers, return the smallest set of indices of numbers such that 
they add up to a target number. You may not use the same element twice.

### Examples

[1,2,6,3,17,82,23,234] -> 26
Solution [3,6]

[1,2,6,3,17,82,23,234] -> 40
Solution [4,6]

[1,2,6,3,17,82,23,234] -> 23
Solution [6]

### Expected limitation and unlimitations

- The algorithm should be able to cope with repeated integers
- Positive integers only

### Further reading

This problem is a slight variation on the classical Knapsack problem. [A lecture slide by Carl Kingsford](https://www.cs.cmu.edu/~ckingsf/class/02713-s13/lectures/lec15-subsetsum.pdf) is attached in this repo for reading.
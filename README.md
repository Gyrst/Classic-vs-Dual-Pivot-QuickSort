# Classic QuickSort vs. Dual Pivot QuickSort Experiment

This paper and experiment was conducted for an assignment in the Applied Algorithms' Class Autumn 2021.


## 1.0 Introduction
quicksort is a heavily used in-place sorting algorithm. It has an average performance of O(nlogn) and is based on a partitioning structure where a pivot is selected and the subsections are sorted recursively. Until recently, the classic implementation of quicksort with a single pivot has shown to be the most efficient. Sedgewick found that the extra overhead created from dual pivot methods outweighed the benefits. However, the recent dual pivot implementation by Yaroslavskiy has proven to show otherwise when implemented and run in Java JVM. Kushagra et al. (2014) later investigated the reasons for the superior performance of the dual pivot implementation and found that it was not the difference in comparison and swap operations that determined the better performance of Yaroslavskiy’s dual pivot implementation, but the significantly fewer cache-misses that the dual pivot approach results in. This papers aims to implement the classic quicksort and Yaroslavskiy’s dual pivot quicksort implementation and test the two against one another in Python 3.8.


## 2.0 Implementation

### 2.1 From Pseudocode to Python
The implementation of the classic and dual pivot algorithms follows the pseudo-code implementations presented in the Wild and Nebel’s paper (2012). However, some adjustment have been made to successfully convert the pseudocode into working python code. Both were written and tested in Python 3.8.10. In the classic quicksort, the do while loops have been handled by creating the variables (counters i, j ) that increment before the inner while loops start, so that i and j increment once before the inner while loops start. Moreover, the outer-while loop is running on the condition while True, and breaks if j > i. For the dual pivot quicksort an initial check if A[left] > A[right] was added to ensure that a swap of the right and left happens if the statement evaluates to true.

### 3.0 Testing for Correctness, Experiments, Discussion and Results

See report pdf for details regarding the experiments and findings.

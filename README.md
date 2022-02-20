# Classic QuickSort vs. Dual Pivot QuickSort Experiment

This paper and experiment was conducted for an assignment in the Applied Algorithms' Class Autumn 2021.


## 1.0 Introduction
quicksort is a heavily used in-place sorting algorithm. It has an average performance of O(nlogn) and is based on a partitioning structure where a pivot is selected and the subsections are sorted recursively. Until recently, the classic implementation of quicksort with a single pivot has shown to be the most efficient. Sedgewick found that the extra overhead created from dual pivot methods outweighed the benefits. However, the recent dual pivot implementation by Yaroslavskiy has proven to show otherwise when implemented and run in Java JVM. Kushagra et al. (2014) later investigated the reasons for the superior performance of the dual pivot implementation and found that it was not the difference in comparison and swap operations that determined the better performance of Yaroslavskiy’s dual pivot implementation, but the significantly fewer cache-misses that the dual pivot approach results in. This papers aims to implement the classic quicksort and Yaroslavskiy’s dual pivot quicksort implementation and test the two against one another in Python 3.8.


# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 06:00:17 2020

@author: Hollarsaint
"""

"""SELECTION SORT ALGORITHM PSEUDOCODE
k = 1
//loop invariant is A[1...k-1] contains a sorted list at all instances.
for j = 1 to n-1 //n is A.length
    least = A[k]
    for i = A[k+1] to A[n]
        if i < least
            least = i
    A[k], A[A.index(least)] = least, A[k]
    k += 1
k += 1 //makes the loop invariant true at termination"""
    
#Python Implementation.
A = [56, 45, 34, 32, 21, 19, 17, 9, 4]        
k = 0
for j in range(len(A)-1):
    least = A[k]
    for i in A[k+1:]:
        if i < least:
            least = i
    A[k], A[A.index(least, k)] = least, A[k]
    k += 1
#A[k], A[A.index(least, k)] = least, A[k]
#print(A)
#k += 1
#print(A)

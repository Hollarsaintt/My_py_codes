# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 06:03:39 2020

@author: Hollarsaint
"""
def countGroups(related):
    # Write your code here
    known = []
    for i in related:
        peoplei  = []
        for people, binary in enumerate(i):
            if binary == '1':
                peoplei.append(people)
        known.append(peoplei)
    known_set = [set(lst) for lst in known]
    for _ in range(len(known_set)):
        for k in known_set:
            for d in known_set[1:]:
                if k.intersection(d) != set():
                    known_set[known_set.index(d)] = k.union(d)
                    known_set.remove(k)
                    break
            break
    try:
        class InputError(Exception): pass
        if set() not in known_set:
            return len(known_set)
        else:
            raise InputError()
    except InputError:
        return 'Error!: You try giving unallowed input'
print(countGroups(['10000', '01000', '00010', '00010', '00001']))
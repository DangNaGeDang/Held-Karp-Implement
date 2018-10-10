#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:59:26 2018

@author: yiminghan
"""
import sys
import numpy as np
import itertools
from copy import deepcopy

def held_karp(dists):



    L = {}

    for k in range(1, nb_vertices):
        L[((k), k)] = (dists[0][k], 0)
    print('L=',L)


    for subset_size in range(2, nb_vertices):
        for subset in itertools.combinations(range(1, nb_vertices), subset_size):

            list_subset=list(int(k) for k in subset)
            # Find the lowest cost to get to this subset
            for k in subset:
                list_subset_prev=deepcopy(list_subset)
                list_subset_prev.remove(k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    if(len(list_subset_prev)==1):
                        
                        res.append((L[((list_subset_prev[0]), m)][0] + dists[m][k], m))
                    else:    
                        res.append((L[(tuple(list_subset_prev), m)][0] + dists[m][k], m))
                L[(tuple(list_subset), k)] = min(res)
                

    list_vertices=list(int(k) for k in range(1,nb_vertices))
    
    # Calculate optimal cost
    res = []
    for k in range(1, nb_vertices):
        res.append((L[(tuple(list_vertices), k)][0] + dists[k][0], k))
    opt, parent = min(res)


    return opt


if __name__ == '__main__':
    
    with open('tsp15.txt') as data_file:
        vertices=[]
        nb_vertices=int(data_file.readline())
        print("expected number of vertices : {0}\n".format(nb_vertices))
        for line in data_file:
            vertices.append(tuple(float(x) for x in line.split()))
    
    vertices=np.array(vertices)
#    print(vertices.shape)
#    print(vertices)

    dists=np.zeros((nb_vertices,nb_vertices))
    for i in range(nb_vertices):
        for j in range(nb_vertices):
            dists[i,j]=np.sqrt(np.sum((vertices[i,:]-vertices[j,:])**2))
            
#    print(dists.shape)
#    print(dists)
#    print(len(dists))
#    print('')
    
    
    print(held_karp(dists))
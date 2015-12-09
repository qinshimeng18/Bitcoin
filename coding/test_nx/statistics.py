# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np
import networkx as nx
from counter import *
from math import *
import matplotlib.pyplot as plt
def drop_zeros(a_list):
    return [i for i in a_list if i>0]

def log_binning(counter_dict,bin_count):

    max_x = log10(max(counter_dict.keys()))
    max_y = log10(max(counter_dict.values()))
    max_base = max([max_x,max_y])

    min_x = log10(min(drop_zeros(counter_dict.keys())))

    bins = np.logspace(min_x,max_base,num=bin_count)
    # Based off of: http://stackoverflow.com/questions/6163334/binning-data-in-python-with-scipy-numpy
    bin_means_y = (np.histogram(counter_dict.keys(),bins,weights=counter_dict.values())[0] / np.histogram(counter_dict.keys(),bins)[0])
    bin_means_x = (np.histogram(counter_dict.keys(),bins,weights=counter_dict.keys())[0] / np.histogram(counter_dict.keys(),bins)[0])

    return bin_means_x,bin_means_y

# ba_g = nx.barabasi_albert_graph(10000,2)
# # print list(bax_g)
# ba_c = nx.degree_centrality(ba_g)
# # print ba_c
# # To convert normalized degrees to raw degrees
# #ba_c = {k:int(v*(len(ba_g)-1)) for k,v in ba_c.iteritems()}
# ba_c2 = dict(Counter(ba_c.values()))
# print ba_c2
# edges=[]
e={}
with open(r'/home/lgn/Downloads/indegree_201207.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        # edge_tuple = (l[0],l[1])
        e[float(l[0])]=float(l[1])
        # edges.append(edge_tuple)
d=dict(e)
# print d

ba_x,ba_y = log_binning(d,20)
# print ba_x,ba_y
# for i in ba_x:
#     print i
# for i in ba_y:
#     print i
# print ba_x
plt.xscale('log')
plt.yscale('log')
plt.scatter(ba_x,ba_y,c='r',marker='s',s=50)
# plt.scatter(d.keys(),d.values(),c='b',marker='x')
plt.xlim((1,1e6))
plt.ylim((1e-6,1e8))
plt.xlabel('Connections (normalized)')
plt.ylabel('Frequency')
plt.show()
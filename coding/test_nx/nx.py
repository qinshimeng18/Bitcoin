# coding: UTF-8
import networkx as nx
import matplotlib.pyplot as plt
import json
import time
# import sys
# from networkx import *
def main():
	"""
	json file format:(you can change the format when you export it from database)
			{
			"RECORDS":[
			{
			"id":10000,
			"source":"1AMxgG5x47coVRRLhrNU3F6htLkb5LbUHq",
			"target":"1FtrEVSSzg2MzFPjcdmCHseVkUMSGNqFTX",
			"weight":0.0122533,
			"time":1368418430
			},----
			]
			}

	"""
	# edges_list=json.load(file(r'14.json'))# python object,not json (decode process) list-> u''
	# #-------------------------------------------
	# edges={}
	# format="%Y-%m-%d"
	# for edge in edges_list['RECORDS']:
	# 	day = time.strftime(format,time.localtime(edge['time']))
	# 	edges[day]=[]
	# for edge in edges_list['RECORDS']:
	# 	edge_tuple = (edge['source'],edge['target'])#,edge['weight']
	# 	day = time.strftime(format,time.localtime(edge['time']))
	# 	edges[day].append(edge_tuple)
	# 	# edges.append(edge_tuple)
	# del edges_list
	# tup_birth = time.localtime(birth_secds)
	# format_birth = time.strftime("%Y-%m-%d",tup_birth)
	# print edges.keys()
	# edges.sort()
	# for key in edges:
	# 	print key # print key,dict[key]

	G=nx.MultiDiGraph()
	G.add_edges_from([(1,1),(1,2)])
	# nx.indegree()
	print  G.in_degree()


	# with open(r'clustering.csv','a') as f:
	# 	for day_key in sorted(edges.keys()):
	# 		G = nx.Graph()
	# 		G.add_edges_from(edges[day_key])
	# 		avg_cluster=nx.average_clustering(G)
	# 		s=day_key+','+str(avg_cluster)+'\n'
	# 		f.write(s)
	# 		del G



		# G = nx.Graph()
		# G.add_edges_from(edges)
	#-----------------------------------
	# edges=[] 1368418430 1447252161
	# for edge in edges_list['RECORDS']:
	# 	edge_tuple = (edge['source'],edge['target'])#,edge['weight']
	# 	edges.append(edge_tuple)
	# del edges_list
	#-----------------------------------
	# #there are diff types of graph
	# G = nx.Graph()
	# # add muti adges into graph=> like [('a','b',0.1),()----]
	# # edges=[]
	# G.add_path([0,1,2,3])
	# G.add_edges_from([(1,4),(1,5),(1,6),(1,7),(4,5)])
	# G.add_edges_from(edges)
	# print G.nodes(),G.edges()
	# #find the arithmetic function you want  example:
	# print G.degree()
	# # if you want to draw pic you can do as fallows 
	# # pos = nx.spectral_layout(G)
	# # nx.draw(G,with_labels=False,node_size = 30)
	# # plt.show()

	# # return a list which index is the degree  and value is the amount 
	# print nx.degree_histogram(G)
	# # print list(nx.all_neighbors(G,1))
	# print nx.clustering(G)
	# # print nx.average_clustering()
#------------------------------------------------
	# degree =  nx.degree_histogram(G)          #返回图中所有节点的度分布序列
	# x = range(len(degree))   #生成x轴序列，从1到最大度
	# y = [z / float(sum(degree)) for z in degree]  
	# print y
	# #将频次转换为频率，这用到Python的一个小技巧：列表内涵，Python的确很方便：）
	# plt.loglog(x,y,color="blue",linewidth=2)  
	# #在双对数坐标轴上绘制度分布曲线  
	# plt.show()      #显示图表
#-------------------------------------
	# RG = nx.random_graphs.random_regular_graph(2,20)  #生成包含20个节点、每个节点有3个邻居的规则图RG
	# pos = nx.spectral_layout(RG)          #定义一个布局，此处采用了spectral布局方式，后变还会介绍其它布局方式，注意图形上的区别
	# nx.draw(RG,pos,with_labels=True,node_size = 30)  #绘制规则图的图形，with_labels决定节点是非带标签（编号），node_size是节点的直径
	# plt.show()  #显示图形  http://www.oschina.net/question/54100_77524
#-------------------------------------
	# path=nx.all_pairs_shortest_path(G)
	# print path['1PBBDUTX68Td9TAp7Z85MHjM5fp9akpRWg']['']
if __name__ == '__main__':
	main()


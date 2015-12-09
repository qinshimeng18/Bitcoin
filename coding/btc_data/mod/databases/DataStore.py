from tables import Nodes,Edges_0910,Edges_2011,Edges_2012,Edges_2013,Edges_2014,Edges_2015,BlkTime

import time

def add_nodes_edges(Txs,block_time,db,path):
	for tx in Txs:
		for input in tx.inputs:
			for output in tx.outputs: 
				# nodes = Nodes(node=input.input_address)
				# nodet = Nodes(node=output.output_address)
				# db.add(nodes)
				# db.add(nodet)
				if int(path[-9:-4]) ==0:
					edge = Edges_0910(source=input.input_address,target=output.output_address,weight=float(output.value)/100000000,time=block_time)
				elif int(path[-9:-4]) <=6:
					edge = Edges_2011(source=input.input_address,target=output.output_address,weight=float(output.value)/100000000,time=block_time)
				elif int(path[-9:-4]) <=34:
					edge = Edges_2012(source=input.input_address,target=output.output_address,weight=float(output.value)/100000000,time=block_time)
				elif int(path[-9:-4]) <=104:
					edge = Edges_2013(source=input.input_address,target=output.output_address,weight=float(output.value)/100000000,time=block_time)
				elif int(path[-9:-4]) <=212:
					edge = Edges_2014(source=input.input_address,target=output.output_address,weight=float(output.value)/100000000,time=block_time)
				elif int(path[-9:-4]) <=263:
					edge = Edges_2015(source=input.input_address,target=output.output_address,weight=float(output.value)/100000000,time=block_time)
				db.add(edge)
				try:
					db.commit()
				except Exception,e:
					db.rollback()
					print e

def blk_time(blknum,blktime,db):
	blktime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(blktime)))
	blk = BlkTime(blk_num=blknum,blk_time=blktime)
	db.add(blk)
	try:
		db.commit()
	except Exception,e:
		db.rollback()
		print e
	
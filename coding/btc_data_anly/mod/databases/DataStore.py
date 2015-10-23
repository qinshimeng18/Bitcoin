from tables import Nodes,Edges,BlkTime

import time

def add_nodes_edges(Txs,block_time,db):
	for tx in Txs:
		for input in tx.inputs:
			for output in tx.outputs:
				# nodes = Nodes(node=input.input_address)
				# nodet = Nodes(node=output.output_address)
				# db.add(nodes)
				# db.add(nodet)
				edge = Edges(source=input.input_address,target=output.output_address,weight=float(output.value)/100000000,time=block_time)
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
	
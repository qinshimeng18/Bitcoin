from ..databases.tables import Nodes,Edges



def add_nodes_edges(Txs,db):
	for tx in self.Txs:
		for input in tx.inputs:
			for output in tx.outputs:
				# nodes = Nodes(node=input.input_address)
				# nodet = Nodes(node=output.output_address)
				# db.add(nodes)
				# db.add(nodet)
				edge = Edges(source=input.input_address,target=output.output_address,weight=float(output.value)/100000000)
				db.add(edge)
				try:
					db.commit()
				except Exception,e:
					db.rollback()
					print e

# def blk_time():
	
# -*- coding: utf-8 -*-
#!/usr/bin/env python
from block import Block
from databases.DataStore import add_nodes_edges,blk_time
class Bitcoin:

	def __init__(self):
		pass
	def analyze(self,path,db):
		"""
		analyze-store
		"""
		print path
		with open(path,'rb') as blockchain:
			# blockchain.seek(100000000,0)
			while True:
				try:
					block = Block(blockchain)
					# block.toString()
					add_nodes_edges(block.Txs,block.blockHeader.time,db,path)
					# blk_time(path[-12:],block.blockHeader.time,db)
					if not block:
						print 'in if'
						break
				except Exception, e:
					print e
					print 'jump one block from dat:',path
					break



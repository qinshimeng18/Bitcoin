#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import traceback  
# import struct
#1¶ÁÈ¡.batÎÄ¼þ2·Ö¸îblock3for¶ÔÃ¿Ò»¸öblock½âÎö4Í·²¿ºÍ½»Ò×²¿·Ö
class Block_value(object):#class to store vars
#----------block---------------------------------------
	num_block=0
	size_block=0
#----------head----------------------------------
	head_block="null"
	version_head="null"
	pre_block_hash="null"
	merkle_root_hash="null"
	time_head=0
	nBits_head="null"
	nonce_head='null'
#-----------tx---------------------------------
	count_tx=0
	version_tx=[]
	num_in_tx=[]
	id_tx=[[]for i in range(2)]
	index_num_tx=[[]for i in range(2)]
	bytes_script=[[]for i in range(2)]
	sig_script=[[]for i in range(2)]
	sequence_tx=[[]for i in range(2)]
	num_out_tx=[]
	satoshis_tx=[[]for i in range(2)]
	bytes_pubkey_script=[[]for i in range(2)]
	pubkey_script=[[]for i in range(2)]
	locktime=[]

	def size(self,str1):#from hex(16H) to 10D ===>int value
		big=0
		for i in range(len(str1)/2):
			l=i*2
			a=str1[l:l+2]
			big+=int(a,16)*16**l# big and small store
		return big
	def tran_bs(self,s_big):# trans from big to small etc: 0d4b to 4b0d=====>string
		# s=s[::-1]
		s_small=""
		n=len(s_big)
		for i in range(n/2):
			s_small=s_small+s_big[n-2*i-2]+s_big[n-2*i-1]
		return s_small

	def tx_set(self,tx):#analyze transaction
		self.count_tx=int(tx[0:2],16)
		self.id_tx=[[]for i in range(self.count_tx)]
		self.index_num_tx=[[]for i in range(self.count_tx)]
		self.bytes_script=[[]for i in range(self.count_tx)]
		self.sig_script=[[]for i in range(self.count_tx)]
		self.sequence_tx=[[]for i in range(self.count_tx)]
		self.satoshis_tx=[[]for i in range(self.count_tx)]
		self.bytes_pubkey_script=[[]for i in range(self.count_tx)]
		self.pubkey_script=[[]for i in range(self.count_tx)]
		# print self.count_tx
		tx=tx[2:]
		#split the transaction
		for i in range(self.count_tx):
			self.version_tx.append(self.tran_bs(tx[0:8]))
			# print tx[0:8]
			tx=tx[8:]
			num_in=self.size(tx[0:2])
			#print num_in
			self.num_in_tx.append(num_in)
			tx=tx[2:]
			for j in range(num_in):
				self.id_tx[i].append(self.tran_bs(tx[0:64]))
				tx=tx[64:]
				self.index_num_tx[i].append(self.tran_bs(tx[0:8]))
				tx=tx[8:]
				bytscript=self.size(tx[0:2])
				self.bytes_script[i].append(bytscript)
				tx=tx[2:]
				self.sig_script[i].append(self.tran_bs(tx[0:2*bytscript]))
				tx=tx[2*bytscript:]
				self.sequence_tx[i].append(self.tran_bs(tx[0:8]))
				tx=tx[8:]
			num_out=self.size(tx[0:2])
			self.num_out_tx.append(num_out)
			tx=tx[2:]
			for k in range(num_out):
				self.satoshis_tx[i].append(self.tran_bs(tx[0:16]))
				tx=tx[16:]
				bytpubkey=self.size(tx[0:2])
				self.bytes_pubkey_script[i].append(bytpubkey)
				tx=tx[2:]
				self.pubkey_script[i].append(tx[0:2*bytpubkey])
				tx=tx[2*bytpubkey:]
			self.locktime.append(self.tran_bs(tx[0:8]))
			tx=tx[8:]

	def head_set(self,h):#analyze head 
		self.version_head=h[0:8]
		self.pre_block_hash=self.tran_bs(h[8:72])#from big to samll
		self.merkle_root_hash=self.tran_bs(h[72:136])
		self.time_head=self.size(h[136:144])
		self.nBits_head=self.tran_bs(h[144:152])
		self.nonce_head=self.tran_bs(h[152:160])

def analyze_block(block,block_obj):#analyze work
	block_obj.head_set(block[0:160])
	block_obj.tx_set(block[160:])
def mysql_init(db):
	sql="""CREATE TABLE head (pre_block_hash VARCHAR(64),
		version_head VARCHAR(8),
		time_head VARCHAR(10),
		nBits_head VARCHAR(8),
		merkle_root_hash VARCHAR(64),
		nonce_head VARCHAR(8),
		num_block VARCHAR(64),
		size_block VARCHAR(64))"""
	try:
		cur=db.cursor()
		cur.execute(sql)
		db.commit
	except Exception,e:
	   # Rollback in case there is any error
	   print str(e )
	   db.rollback()
	   print "exception in mysql_init"
def mysql_exe(db,block_obj):
	try:
		cur=db.cursor()
		values=[]
		for i in range(1):
			values.append((block_obj.pre_block_hash,
		block_obj.version_head,
		str(block_obj.time_head),
		block_obj.nBits_head,
		block_obj.merkle_root_hash,
		block_obj.nonce_head,
		block_obj.num_block,
		block_obj.size_block))
		cur.executemany('INSERT INTO head VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',values)
		db.commit()
	except Exception,e:
	   # Rollback in case there is any error
	   print str(e )
	   print traceback.print_exc()  
	   db.rollback()
	   print "exception in mysql_exe"

def write_som(block_obj,t):#write or print or insert database someting
        t.write("time:  "+str(block_obj.time_head)+'\tid_tx:  '+str(block_obj.id_tx)+"\n")

def main_fun():
	f = open(r'/home/lgn/Desktop/blk00000.dat','rb')#open
	db=MySQLdb.connect("localhost","root","qsm199549",'btc') # create database btc;,'btc'
	mysql_init(db)
	blocks_bit=f.read()#store binary stream file type==string
	blocks_hex=blocks_bit.encode('hex')#store hex type==string
	blocks_list=blocks_hex.split('f9beb4d9')[1:]# cut the whole file into tens of thousands of blocks type==tuple

	block_obj=Block_value() #create object

	t=open('./remod.txt','w')#txt like database
	val=0
	block_obj.num_block=len(blocks_list)-1#numbers of blocks

	for block in blocks_list:# analyze block
		block_obj.size_block=block_obj.size(blocks_list[val][:8])#block size
		analyze_block(blocks_list[val][8:],block_obj)#do work
		# write_som(block_obj,t)#store info you like
		val=val+1
		mysql_exe(db,block_obj)
	print "work over"
	
	
	db.close()
	print 'sql over'
	t.close()
	f.close()   

if __name__ == '__main__':#easy to import cut mudle
	main_fun()#begin

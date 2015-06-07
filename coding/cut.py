#!/usr/bin/env python
import struct
#1读取.bat文件2分割block3for对每一个block解析4头部和交易部分
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
	version_tx='null'

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

	def tx_set(self,tx):#analyze tansction
		self.count_tx=int(tx[0:2],16)
		self.version_tx=tx[2:10]

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
	
def write_som(block_obj,t):#write or print or insert database someting  'block_hash:'+block_obj.merkle_root_hash+
	t.write('\tpre_block: '+block_obj.pre_block_hash+'\tcount_tx:'+str(block_obj.count_tx)+"\ttime:"+str(block_obj.time_head)+"\n")

def main_fun():
	f = open('/home/lgn/Desktop/blk00000.dat','rb')#open
	# print type(f.read(4))
	# print struct.unpack("i",f.read(4))#another way to count size
	blocks_bit=f.read()#store binary stream file type==string
	blocks_hex=blocks_bit.encode('hex')#store hex type==string
	blocks_list=blocks_hex.split('f9beb4d9')[1:]# cut the whole file into tens of thousands of blocks type==tuple

	block_obj=Block_value() #create object

	t=open('./re.txt','w')#txt like database
	val=0
	block_obj.num_block=len(blocks_list)-1#numbers of blocks

	for block in blocks_list:# analyze block
		block_obj.size_block=block_obj.size(blocks_list[val][:8])#block size
		analyze_block(blocks_list[val][8:],block_obj)#do work
		write_som(block_obj,t)#store info you like
		val=val+1
	print "work over"
	t.close()
	f.close()   

if __name__ == '__main__':#easy to import cut mudle
	main_fun()#begin

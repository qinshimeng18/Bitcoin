# -*- coding: utf-8 -*-
#!/usr/bin/env python
from mod.blocktools import *
from sqlalchemy.orm import scoped_session, sessionmaker
from mod.databases.db import engine
from mod.bitcoin import Bitcoin
import os,sys

def main():
	db = scoped_session(sessionmaker(bind=engine,
                        autocommit=False, autoflush=True,
                        expire_on_commit=False))
	# path = r'/home/lgn/Desktop/blk00000.dat'
	print 'please input number form 00000 to 00263'
	# start = sys.stdin.readline()
	# end = sys.stdin.readline()
	#input start number and end number
	start = input("input start number")
	end = input("input end number")
	for path,dirs,files in os.walk(r"C:\Users\xy2\Desktop\blocks"):
		for file in files:
			if file.endswith(".dat"):
				p=os.path.join(path,file)
				if int(p[-9:-4])<= end and int(p[-9:-4])>= start:
					blk_dat = Bitcoin().analyze(p,db)
					del blk_dat
					print p,'\tis ok!'
	print "over"


if __name__ == '__main__':
	main()



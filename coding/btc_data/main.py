# -*- coding: utf-8 -*-
#!/usr/bin/env python
from mod.blocktools import *
from sqlalchemy.orm import scoped_session, sessionmaker
from mod.databases.db import engine
from mod.bitcoin import Bitcoin
import os

def main():
	db = scoped_session(sessionmaker(bind=engine,
                        autocommit=False, autoflush=True,
                        expire_on_commit=False))
	# path = r'/home/lgn/Desktop/blk00000.dat'
	for path,dirs,files in os.walk(r"C:\Users\xy2\Desktop\blocks"):
		for file in files:
			if file.endswith(".dat"):
				blk_dat = Bitcoin().analyze(os.path.join(path,file),db)
				del blk_dat
				print os.path.join(path,file),'\tis ok!'
	print "over"


if __name__ == '__main__':
	main()
	
	

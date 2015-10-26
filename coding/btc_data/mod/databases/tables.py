#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, VARCHAR,ForeignKey, Float 
from sqlalchemy.orm import relationship,backref
from db import engine,Base

class Nodes(Base):
	__tablename__ = 'nodes'
	id = Column(Integer,primary_key=True)
	# id = Column(VARCHAR(64),primary_key=True)
	node = Column(VARCHAR(64))

class Edges_0910(Base):
	__tablename__ = 'edges_0910'
	id = Column(Integer,primary_key=True)
	# source = Column(VARCHAR(64),ForeignKey('nodes.node', ondelete='CASCADE'))
	source = Column(VARCHAR(64))
	target = Column(VARCHAR(64))
	weight = Column(Float)
	time = Column(VARCHAR(64))

class Edges_2011(Base):
	__tablename__ = 'edges_2011'
	id = Column(Integer,primary_key=True)
	# source = Column(VARCHAR(64),ForeignKey('nodes.node', ondelete='CASCADE'))
	source = Column(VARCHAR(64))
	target = Column(VARCHAR(64))
	weight = Column(Float)
	time = Column(VARCHAR(64))
class Edges_2012(Base):
	__tablename__ = 'edges_2012'
	id = Column(Integer,primary_key=True)
	# source = Column(VARCHAR(64),ForeignKey('nodes.node', ondelete='CASCADE'))
	source = Column(VARCHAR(64))
	target = Column(VARCHAR(64))
	weight = Column(Float)
	time = Column(VARCHAR(64))
class Edges_2013(Base):
	__tablename__ = 'edges_2013'
	id = Column(Integer,primary_key=True)
	# source = Column(VARCHAR(64),ForeignKey('nodes.node', ondelete='CASCADE'))
	source = Column(VARCHAR(64))
	target = Column(VARCHAR(64))
	weight = Column(Float)
	time = Column(VARCHAR(64))
class Edges_2014(Base):
	__tablename__ = 'edges_2014'
	id = Column(Integer,primary_key=True)
	# source = Column(VARCHAR(64),ForeignKey('nodes.node', ondelete='CASCADE'))
	source = Column(VARCHAR(64))
	target = Column(VARCHAR(64))
	weight = Column(Float)
	time = Column(VARCHAR(64))
class Edges_2015(Base):
	__tablename__ = 'edges_2015'
	id = Column(Integer,primary_key=True)
	# source = Column(VARCHAR(64),ForeignKey('nodes.node', ondelete='CASCADE'))
	source = Column(VARCHAR(64))
	target = Column(VARCHAR(64))
	weight = Column(Float)
	time = Column(VARCHAR(64))
class BlkTime(Base):
	__tablename__ = 'BlkTime'
	id = Column(Integer,primary_key=True)

	blk_num	= Column(VARCHAR(64))
	blk_time = Column(VARCHAR(64))
